# sample2.py
# Parse a requirements.txt file and list missing dependencies

import pkgutil


def is_installed(package):
    return pkgutil.find_loader(package) is not None


def check_requirements(requirements):
    for pkg in requirements:
        pkg = pkg.strip()
        if not pkg or pkg.startswith("#"):
            continue
        name = pkg.split("==")[0]
        print(pkg, "->", "installed" if is_installed(name) else "missing")


def main():
    requirements = [
        "numpy==1.24.0",
        "nonexistent-package==0.0.1",
    ]
    check_requirements(requirements)


if __name__ == "__main__":
    main()
