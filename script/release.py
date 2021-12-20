#! /usr/bin/env python3
import build_utils, common, os, sys

def main():
  os.chdir(common.basedir)
  version = common.version()

  for classifier in ["", "-sources", "-javadoc"]:
      build_utils.deploy(f"target/skija-shared-{version}{classifier}.jar", tempdir = "shared/target/deploy")

  for system in ['windows', 'linux', 'macos-x64', 'macos-arm64']:
    for classifier in ["", "-sources", "-javadoc"]:
      build_utils.deploy(f"target/skija-{system}-{version}{classifier}.jar", tempdir = "platform/target/deploy")

  build_utils.release()

  return 0

if __name__ == "__main__":
  sys.exit(main())