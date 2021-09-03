# 557_test_on_gem5

Running 557.xz_r of SPEC2017 with a small test file, in a simple system on gem5.

- `static_xz_r`: an statically compiled executable file
- `smallf.tar.xz`: the test compressed file
- `557simple.py`: the gem5 configuration file

**Under the repo directory**

to simulate on gem5 (it might take about 10 mins), run

```
PATH_TO_YOUR_gem5.opt 557simple
```

to test directly on the host machine (it should only take several seconds), run

```
./static_xz_r smallf.tar.xz 1 12eff5edf0b5994e554f5210e043b59518234486281a4c9830eb5e8edb14d65ebf9d0f66b9659e4b6db7b0dc458129a60d77e7a750b7b34ef67b02229ef6588e 1000 3000 3
```
