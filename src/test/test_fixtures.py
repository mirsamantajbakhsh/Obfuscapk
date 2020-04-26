#!/usr/bin/env python3

import shutil
from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def tmp_working_directory_path(tmp_path_factory) -> str:
    """
    Return a path to a temporary working directory (different path for each test).
    """
    return str(tmp_path_factory.mktemp("obfuscation_working_dir"))


@pytest.fixture(scope="function")
def tmp_demo_apk_v10_original_path(tmp_path) -> str:
    """
    Return a path to a valid demo apk file generated with Android Studio (different
    path for each test, but the apk file is the same).
    """
    source = (
        Path(__file__)
        .resolve()
        .parent.joinpath(
            "test_resources", "v1.0", "com.obfuscapk.demo.v1.0-original.apk"
        )
    )
    destination = tmp_path.joinpath("com.obfuscapk.demo.v1.0-original.apk")
    destination = shutil.copy2(source, destination)
    return str(destination)


@pytest.fixture(scope="function")
def tmp_demo_apk_v10_rebuild_path(tmp_path) -> str:
    """
    Return a path to a valid demo apk file generated with Apktool (different path for
    each test, but the apk file is the same). This can be useful to test signing and
    aligning.
    """
    source = (
        Path(__file__)
        .resolve()
        .parent.joinpath(
            "test_resources", "v1.0", "com.obfuscapk.demo.v1.0-rebuild.apk"
        )
    )
    destination = tmp_path.joinpath("com.obfuscapk.demo.v1.0-rebuild.apk")
    destination = shutil.copy2(source, destination)
    return str(destination)
