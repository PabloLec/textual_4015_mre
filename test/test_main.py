import pytest

from textual_4015_mre import DemoApp


@pytest.mark.asyncio
async def test_app():
    async with DemoApp().run_test() as pilot:
        assert pilot.app is not None
        assert pilot.app.screen is not None
