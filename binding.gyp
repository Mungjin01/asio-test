{
  "targets": [
    {
      "target_name": "asioaddon",
      "sources": [
        "src/asioaddon.cpp",
        "src/asio_driver.cpp",
        "src/asio_driver.h",
        "ASIO_SDK/common/asio.cpp",
        "ASIO_SDK/host/asiodrivers.cpp",
        "ASIO_SDK/host/pc/asiolist.cpp",
        "ASIO_SDK/host/pc/asiolist.h",
        "ASIO_SDK/host/pc/asiolist.cpp",
        "ASIO_SDK/common/asio.cpp",
        "ASIO_SDK/common/asio.h",
      ],
      "include_dirs": [
        "<!(node -e \"require('node-addon-api').include\")",
         "ASIOSDK/asio",
          "ASIOSDK/common",
          "ASIOSDK/host",
      ],
      "dependencies": [
        "<!(node -e \"require('node-addon-api').gyp\")"
      ],
      "cflags": [ "-std=c++11" ],
      "cflags!": [ "-fno-exceptions" ]
    }
  ]
}
