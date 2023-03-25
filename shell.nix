{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = [
        pkgs.git
        pkgs.python310Full
        pkgs.python310Packages.pandas
        pkgs.poetry
        pkgs.zsh
        pkgs.mysql80
        pkgs.wget
    ];
}
