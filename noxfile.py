import nox

nox.options.default_venv_backend = "uv"
nox.options.error_on_external_run = True
nox.options.sessions = ["lint", "type_check"]


@nox.session(venv_backend="none")
def lint(session: nox.Session) -> None:
    """Check for linter issues and if the code is formatted correctly."""
    session.run("ruff", "check", "--no-fix")
    session.run("ruff", "format", "--check")


@nox.session(venv_backend="none")
def tidy(session: nox.Session) -> None:
    """Automatically fix any fixable linter issues and format the code."""
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session(venv_backend="none")
def type_check(session: nox.Session) -> None:
    """Check for type issues."""
    session.run("pyright")
