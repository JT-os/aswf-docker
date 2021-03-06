# Copyright (c) Contributors to the aswf-docker Project. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Main configuration and constants for aswfdocker
"""
import enum

from aswfdocker import versioninfo


class ImageType(enum.Enum):
    IMAGE = "image"
    PACKAGE = "package"


VERSIONS = {
    ImageType.PACKAGE: {
        "clang": ["1.1"],
        "ninja": ["1.2"],
        "python": ["2018.1", "2019.1", "2020.1"],
        "boost": ["2018.1", "2019.1", "2020.1"],
        "tbb": ["2018.1", "2019.1", "2020.1"],
        "cppunit": ["2018.1", "2019.1", "2020.1"],
        "glew": ["2018.1", "2019.1", "2020.1"],
        "glfw": ["2018.1", "2019.1", "2020.1"],
        "log4cplus": ["2018.1", "2019.1", "2020.1"],
        "qt": ["2018.1", "2019.1", "2020.1"],
        "pyside": ["2018.1", "2019.1", "2020.1"],
        "blosc": ["2018.1", "2019.1", "2020.1"],
        "openexr": ["2018.1", "2019.1", "2020.1"],
        "alembic": ["2018.1", "2019.1", "2020.1"],
        "ocio": ["2018.1", "2019.1", "2020.1"],
        "oiio": ["2018.1", "2019.1", "2020.1"],
        "opensubdiv": ["2018.1", "2019.1", "2020.1"],
        "ptex": ["2018.1", "2019.1", "2020.1"],
        "openvdb": ["2019.1", "2020.1"],
        "usd": ["2019.2", "2020.1"],
        "partio": ["2018.0", "2019.0", "2020.0"],
        "osl": ["2018.0", "2019.0", "2020.0"],
    },
    ImageType.IMAGE: {
        "common": ["1.4"],
        "base": ["2018.4", "2019.4", "2020.4"],
        "openexr": ["2018.4", "2019.4", "2020.4"],
        "openvdb": ["2018.4", "2019.4", "2020.4"],
        "ocio": ["2018.5", "2019.5", "2020.4"],
        "opencue": ["2018.4", "2019.4", "2020.4"],
        "usd": ["2019.5", "2020.4"],
        "osl": ["2018.0", "2019.0", "2020.0"],
        "vfxall": ["2019.6", "2020.4"],
    },
}

GROUPS = {
    ImageType.PACKAGE: {
        "common": ["clang", "ninja"],
        "base": ["python", "boost", "tbb", "cppunit", "glew", "glfw", "log4cplus"],
        "baseqt": ["qt"],
        "basepyside": ["pyside"],
        "vfx": [
            "blosc",
            "openexr",
            "alembic",
            "ocio",
            "oiio",
            "opensubdiv",
            "ptex",
            "openvdb",
            "usd",
            "partio",
            "osl",
        ],
    },
    ImageType.IMAGE: {
        "common": ["common"],
        "base": ["base"],
        "openexr": ["openexr"],
        "openvdb": ["openvdb"],
        "osl": ["osl"],
        "opencue": ["opencue"],
        "ocio": ["ocio"],
        "usd": ["usd"],
        "vfxall": ["vfxall"],
    },
}

VERSION_INFO = {
    "1": versioninfo.VersionInfo(
        major_version="1", label="latest", ci_common_version="1", python_version="2.7",
    ),
    "2018": versioninfo.VersionInfo(
        major_version="2018", label=None, ci_common_version="1", python_version="2.7",
    ),
    "2019": versioninfo.VersionInfo(
        major_version="2019",
        label="latest",
        ci_common_version="1",
        python_version="2.7",
    ),
    "2020": versioninfo.VersionInfo(
        major_version="2020",
        label="preview",
        ci_common_version="1",
        python_version="3.7",
    ),
}

PUBLISH_DOCKER_ORG = "aswf"
TESTING_DOCKER_ORG = "aswftesting"
# this org is not valid, but this ensures that the test will not accidently pull an existing image
FAKE_DOCKER_ORG = "aswflocaltesting"

DOCKER_REGISTRY = "docker.io"

DEV_BUILD_DATE = "dev"
DEV_VCS_REF = "dev"

MAIN_GITHUB_ASWF_DOCKER_URL = "https://github.com/AcademySoftwareFoundation/aswf-docker"
