import aiohttp_jinja2
import jinja2
from aiohttp import web
from decouple import config


APP_PORT = config("APP_PORT", cast=int)


class IndexView(web.View):
    @aiohttp_jinja2.template("index.jinja2")
    async def get(self):
        return {}

    @aiohttp_jinja2.template("index.jinja2")
    async def post(self):
        data = await self.request.post()
        return {"username": data["username"]}


def build_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader("templates"),
    )
    app.add_routes([
        web.view("/", IndexView),
    ])
    return app


if __name__ == "__main__":
    web.run_app(build_app(), port=APP_PORT)
