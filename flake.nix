{
  description = "Barbs dev shell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-24.11";
  };

  outputs =
    { nixpkgs, ... }:
    let
      pkgs = nixpkgs.legacyPackages."x86_64-linux";
    in
    {
      devShells."x86_64-linux".default = pkgs.mkShell {

        packages = [
          pkgs.python312

          # imports
          pkgs.python312Packages.matplotlib
          pkgs.python312Packages.numpy
          pkgs.python312Packages.seaborn

          pkgs.figlet
          pkgs.lolcat
        ];

        shellHook = ''
          clear

            # echo "barbetta coding time" | lolcat -a -d 64 -p 1 -F 0.2

            printf "██████╗  █████╗ ██████╗ ██████╗     ████████╗██╗███╗   ███╗███████╗\n██╔══██╗██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██║████╗ ████║██╔════╝\n██████╔╝███████║██████╔╝██████╔╝       ██║   ██║██╔████╔██║█████╗  \n██╔══██╗██╔══██║██╔══██╗██╔══██╗       ██║   ██║██║╚██╔╝██║██╔══╝  \n██████╔╝██║  ██║██║  ██║██████╔╝       ██║   ██║██║ ╚═╝ ██║███████╗\n╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝        ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝\n" | lolcat -S 48 -a -s 80
        '';
      };
    };
}
