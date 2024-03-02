from molotov import scenario


from generator.generator_person_data import generate_person_data
from logging_config import configure_logger

logger = configure_logger(__name__, "test.log")

_API = "http://127.0.0.1:8000/tasks"


@scenario(weight=40)
async def test_get_tasks(session):
    try:
        async with session.get(_API) as resp:
            assert resp.status == 200, resp.status
            assert (
                resp.headers["content-type"] == "application/json"
            ), "Unexpected content type: {}".format(resp.headers["content-type"])
    except Exception as e:
        logger.error(f"An error occurred: {e}")


@scenario(weight=60)
async def test_post_task(session):
    try:
        person = generate_person_data()
        async with session.post(
            f"{_API}?name={person.name}&description={person.description}"
        ) as resp:
            assert resp.status == 200, resp.status
            assert (
                resp.headers["content-type"] == "application/json"
            ), "Unexpected content type: {}".format(resp.headers["content-type"])
            body = await resp.json()
            assert "ok" in body, "Response body does not contain 'ok'"
            assert "task_id" in body, "Response body does not contain 'task_id'"
    except Exception as e:
        logger.error(f"An error occurred: {e}")
