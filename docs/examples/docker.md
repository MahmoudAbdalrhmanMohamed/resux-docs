# Docker Deployment Example

Generate the maintained Docker files:

```sh
resux deploy . --preset docker
```

Review the generated `Dockerfile`, `.dockerignore`, and `DEPLOYMENT.md` before deploying.

## Build

Provide the report signing secret to BuildKit from your CI secret store or shell environment. Do not pass it through `ARG` or `--build-arg`.

```sh
DOCKER_BUILDKIT=1 docker build \
  --secret id=resux_halal_report_signing_secret,env=RESUX_HALAL_REPORT_SIGNING_SECRET \
  -t resux-app .
```

Consume the secret only in the build step that needs it:

```dockerfile
RUN --mount=type=secret,id=resux_halal_report_signing_secret \
  RESUX_HALAL_REPORT_SIGNING_SECRET="$(cat /run/secrets/resux_halal_report_signing_secret)" \
  npm run build
```

BuildKit mounts the value temporarily for that `RUN` instruction instead of storing it as a Docker build argument or image environment variable. Do not copy the mounted secret into the image filesystem.

## Run

The generated production guard also needs the same secret at runtime. Inject it through your platform's runtime secret manager or environment configuration:

```sh
docker run --rm \
  -p 3000:3000 \
  -e PORT=3000 \
  -e RESUX_HALAL_REPORT_SIGNING_SECRET \
  resux-app
```

The final `-e` reads the value from the host environment without placing a literal secret in the command.

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
