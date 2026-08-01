# Docker Deployment Example

Generate the maintained Docker files:

```sh
resux deploy . --preset docker
```

Review the generated `Dockerfile`, `.dockerignore`, and `DEPLOYMENT.md` before deploying.

## Build

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET='private-random-secret-at-least-32-characters'
docker build \
  --build-arg RESUX_HALAL_REPORT_SIGNING_SECRET="$RESUX_HALAL_REPORT_SIGNING_SECRET" \
  -t resux-app .
```

Avoid baking long-lived secrets into image layers. Prefer your CI platform's secret mounts/build secrets and pass the same report verification secret securely at runtime when required by the generated production guard.

## Run

```sh
docker run --rm \
  -p 3000:3000 \
  -e PORT=3000 \
  -e RESUX_HALAL_REPORT_SIGNING_SECRET="$RESUX_HALAL_REPORT_SIGNING_SECRET" \
  resux-app
```

## Health check

```txt
GET /__resux/health
```

## Production checklist

- run as a non-root user where practical,
- use a read-only filesystem except required cache/temp paths,
- set memory/CPU limits,
- terminate TLS at a trusted proxy or platform,
- configure logs and graceful shutdown,
- protect environment variables,
- and scan the final image and dependency tree.
