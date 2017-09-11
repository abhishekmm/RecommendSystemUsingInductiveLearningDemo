<<<<<<< HEAD
# Description:
# Transfer learning example for TensorFlow.

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

load("//tensorflow:tensorflow.bzl", "py_test")

py_binary(
    name = "retrain",
    srcs = [
        "label_image.py",
    ],
    srcs_version = "PY2AND3",
    visibility = ["//tensorflow:__subpackages__"],
    deps = [
        "//tensorflow:tensorflow_py",
        "//tensorflow/python:framework",
        "//tensorflow/python:framework_for_generated_wrappers",
        "//tensorflow/python:platform",
        "//tensorflow/python:util",
        "//third_party/py/numpy",
    ],
)

py_binary(
    name = "label_image",
    srcs = [
        "label_image.py",
    ],
    srcs_version = "PY2AND3",
    visibility = ["//tensorflow:__subpackages__"],
    deps = [
        "//tensorflow:tensorflow_py",
    ],
)

py_test(
    name = "retrain_test",
    size = "small",
    srcs = [
        "label_image.py",
        "retrain.py",
    ],
    data = [
        ":retrained_labels.txt",
        "//tensorflow/examples/method3mod/dataset/dataset/T/ShirtCollar:data/1.jpg",
    ],
    srcs_version = "PY2AND3",
    deps = [
        ":retrain",
        "//tensorflow:tensorflow_py",
        "//tensorflow/python:framework_test_lib",
        "//tensorflow/python:platform_test",
    ],
)

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
        ],
    ),
    visibility = ["//tensorflow:__subpackages__"],
)
=======
# Description:
# Transfer learning example for TensorFlow.

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

load("//tensorflow:tensorflow.bzl", "py_test")

py_binary(
    name = "retrain",
    srcs = [
        "label_image.py",
    ],
    srcs_version = "PY2AND3",
    visibility = ["//tensorflow:__subpackages__"],
    deps = [
        "//tensorflow:tensorflow_py",
        "//tensorflow/python:framework",
        "//tensorflow/python:framework_for_generated_wrappers",
        "//tensorflow/python:platform",
        "//tensorflow/python:util",
        "//third_party/py/numpy",
    ],
)

py_binary(
    name = "label_image",
    srcs = [
        "label_image.py",
    ],
    srcs_version = "PY2AND3",
    visibility = ["//tensorflow:__subpackages__"],
    deps = [
        "//tensorflow:tensorflow_py",
    ],
)

py_test(
    name = "retrain_test",
    size = "small",
    srcs = [
        "label_image.py",
        "retrain.py",
    ],
    data = [
        ":retrained_labels.txt",
        "//tensorflow/examples/method3mod/dataset/dataset/T/ShirtCollar:data/1.jpg",
    ],
    srcs_version = "PY2AND3",
    deps = [
        ":retrain",
        "//tensorflow:tensorflow_py",
        "//tensorflow/python:framework_test_lib",
        "//tensorflow/python:platform_test",
    ],
)

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
        ],
    ),
    visibility = ["//tensorflow:__subpackages__"],
)
>>>>>>> ba84b7d6234a962fe8d0186a07338684f1d6e918
