"""Install metadata for older pip that mishandles PEP 621-only layouts."""

from setuptools import setup

setup(
    name="skill-box",
    version="0.1.0",
    description="CLI tool: skill_box command",
    packages=["skill_box"],
    package_dir={"": "src"},
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "skill_box = skill_box.cli:main",
        ],
    },
)
