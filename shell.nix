with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv {
    name = name;
    paths = buildInputs;
  };
  buildInputs = [
    python3
    python3Packages.feedgen

    # Testing things
    python3Packages.epc
    python3Packages.flake8
    python3Packages.jedi
  ];
}
