from settings.settings import DevConfig
import app


def run(api):
    api.run()


if __name__ == "__main__":
    api = app.create_app(DevConfig)
    run(api)