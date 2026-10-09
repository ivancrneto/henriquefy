def test_settings_import():
    import settings

    assert settings.DEBUG is None or isinstance(settings.DEBUG, str)
