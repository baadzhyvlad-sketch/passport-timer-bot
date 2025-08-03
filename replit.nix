{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.wheel
    pkgs.python311Packages.apscheduler
    pkgs.python311Packages.pythonTelegramBot
    pkgs.python311Packages.pytz
  ];
}
