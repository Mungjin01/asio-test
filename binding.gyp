{
  "targets": [
    {
      "target_name": "asioaddon",
      "sources": [
        "src/asioaddon.cpp"
      ],
      "include_dirs": [
        "<!(node -e \"require('node-addon-api').include\")"
      ],
      "dependencies": [
        "<!(node -e \"require('node-addon-api').gyp\")"
      ],
      "cflags": [ "-std=c++11" ],
      "cflags!": [ "-fno-exceptions" ]
    }
  ]
}
