# Threat Management API

Containerized .NET 9 / F# Minimal API for reporting and querying threats found on managed assets.

## Stack

- .NET 9, F# Minimal API
- EF Core 9 + SQLite (one file, `EnsureCreated()` — no migrations needed)
- Linux container, non-root user, HTTPS-only on port 8443

## Architecture

Tiered, dependency direction: `TM.API → TM.Services → TM.Data → TM.Core`

| Layer | Project | Files |
|-------|---------|-------|
| Domain types + service interfaces | `TM.Core` | `Domain.fs`, `Services.fs` |
| EF Core entities + DbContext | `TM.Data` | `DataTypes.fs`, `TmDbContext.fs` |
| IThreatService implementation | `TM.Services` | `ThreatService.fs` |
| DTOs, mediator, entry point | `TM.API` | `Contracts.fs`, `Mediator.fs`, `Program.fs` |

DI and a custom `IMediator` (not MediatR) decouple route handlers from services.

## Domain Types

```fsharp
type ThreatClassification = PUP | Malware | Ransomware
type ThreatAction         = Terminated | Waived | NoAction  // serialises to "None"; NOT named None (shadows Option.None)

type FileHash = { SHA1: string; SHA256: string; MD5: string }

type Threat = {
    Id: Guid; AssetId: string
    Hashes: FileHash list       // stored as JSON string in SQLite
    FileNames: string list      // stored as JSON string in SQLite
    PID: int option
    Classification: ThreatClassification
    Action: ThreatAction
    FoundAt: DateTimeOffset; ReportedAt: DateTimeOffset
}
```

EF Core entity (`[<CLIMutable>]` record) mirrors `Threat` but uses `HashesJson: string`, `FileNamesJson: string`, and `PID: Nullable<int>`.

## Routes

| Method | Path | Success | Notes |
|--------|------|---------|-------|
| POST | `/threats` | 201 + ThreatResponse | Report a threat |
| GET | `/threats?assetId={id}` | 200 + ThreatListResponse | 400 if `assetId` missing |
| GET | `/threats/{id:guid}` | 200 + ThreatResponse | 404 if not found |
| GET | `/openapi/v1.json` | 200 | Spec only, no UI |

## Requirements

**Functional**
- No authentication
- Compressed output (`AddResponseCompression`)
- JSON-only (camelCase, `WhenWritingNull`)

**Security**
- HTTPS only (Kestrel TLS 1.2+); cert via env vars `ASPNETCORE_Kestrel__Certificates__Default__Path` / `__Password`
- HTTP-only cookies, `Secure`, `SameSite=Lax`
- Response headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer`, `Cache-Control: no-store`, `Content-Security-Policy: default-src 'none'`, remove `Server`
- Container runs as non-root (`appuser`)
