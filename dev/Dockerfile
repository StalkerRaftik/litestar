FROM python:3.12

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry
RUN poetry --version

# python dependencies
COPY ../pyproject.toml ../poetry.lock* /
RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-interaction --no-ansi


WORKDIR /src

ENTRYPOINT ["/bin/bash", "-c", "source /.venv/bin/activate && exec \"$@\"", "--"]
