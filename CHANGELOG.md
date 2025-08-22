# Changelog

## 0.1.0-alpha.6 (2025-08-22)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/cruzluna/sps-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* clean up environment call outs ([fd11684](https://github.com/cruzluna/sps-python/commit/fd11684a479d5bd40ae9b58921b29c95513063a4))
* **client:** support file upload requests ([fdb7367](https://github.com/cruzluna/sps-python/commit/fdb7367507dca652dfa88ab1eccd254e7201b73d))


### Bug Fixes

* **ci:** correct conditional ([372a857](https://github.com/cruzluna/sps-python/commit/372a857bfac2a4c6d705b4bbdc045f85271afc4e))
* **ci:** release-doctor — report correct token name ([5b09aa7](https://github.com/cruzluna/sps-python/commit/5b09aa7c1ee6c4425d779e1ab740168a2af05362))
* **client:** don't send Content-Type header on GET requests ([6838055](https://github.com/cruzluna/sps-python/commit/6838055c08e18543cca8929a63d637402df35419))
* **parsing:** correctly handle nested discriminated unions ([d60df6e](https://github.com/cruzluna/sps-python/commit/d60df6e6ee08738e27d94e108870b52935d6d4c6))
* **parsing:** ignore empty metadata ([71b7233](https://github.com/cruzluna/sps-python/commit/71b7233514cf47dc0a883356e3c892c094b455e6))
* **parsing:** parse extra field types ([b51d5a5](https://github.com/cruzluna/sps-python/commit/b51d5a5f9465380b3fc4d157d7cc9849a8c02acf))


### Chores

* **ci:** change upload type ([82ccbb3](https://github.com/cruzluna/sps-python/commit/82ccbb3bd2ae4de0d7366646df400db928480af0))
* **ci:** only run for pushes and fork pull requests ([dad3aeb](https://github.com/cruzluna/sps-python/commit/dad3aeb7544d8ff189d5da072914dc6335f1a693))
* **internal:** bump pinned h11 dep ([2b91465](https://github.com/cruzluna/sps-python/commit/2b91465bf5a1a18af230556e50b097fbe2763092))
* **internal:** codegen related update ([3fc8d64](https://github.com/cruzluna/sps-python/commit/3fc8d642684e2775eac6cdb1fe601699eae44aea))
* **internal:** codegen related update ([5360340](https://github.com/cruzluna/sps-python/commit/5360340a2c9b9fa79d6c439c4f8992eb12067fb7))
* **internal:** fix ruff target version ([8edf214](https://github.com/cruzluna/sps-python/commit/8edf214f4739d22963bb6b5fdf8ae4dbb552b36e))
* **internal:** update comment in script ([f1c6869](https://github.com/cruzluna/sps-python/commit/f1c6869453fe8ada85a696b9d18038494d9f4b95))
* **package:** mark python 3.13 as supported ([c13f9a1](https://github.com/cruzluna/sps-python/commit/c13f9a1b41aa5162e2208f99acd677285db9fcf5))
* **project:** add settings file for vscode ([fe01959](https://github.com/cruzluna/sps-python/commit/fe019595ddadb5b4cef7d202290310eb0b4890b8))
* **readme:** fix version rendering on pypi ([ebf7fd1](https://github.com/cruzluna/sps-python/commit/ebf7fd1263b30dc49e2d2dbe5d108df95033e2c0))
* update @stainless-api/prism-cli to v5.15.0 ([95de321](https://github.com/cruzluna/sps-python/commit/95de32139b58a9e4adbcdfdcec1c4e5b090c1248))
* update github action ([7a2373d](https://github.com/cruzluna/sps-python/commit/7a2373d85ce0d8397d905909f8c8397c4b401fb2))

## 0.1.0-alpha.5 (2025-06-24)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/cruzluna/sps-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **client:** add support for aiohttp ([fe48770](https://github.com/cruzluna/sps-python/commit/fe487703a75e996e245834f623ade3e8bd2f2860))


### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([c5eb2c7](https://github.com/cruzluna/sps-python/commit/c5eb2c7622aa562a5563186c8bb9ffb8ed2ea3bb))


### Chores

* **ci:** enable for pull requests ([1ce48f3](https://github.com/cruzluna/sps-python/commit/1ce48f39a477414e71ac78527fbd28d895b1c977))
* **internal:** update conftest.py ([d340781](https://github.com/cruzluna/sps-python/commit/d340781c57ca746c78fbe4dd14d642596007c681))
* **readme:** update badges ([be13d2f](https://github.com/cruzluna/sps-python/commit/be13d2f05df26758a37a08a1cdf07ab286c348ed))
* **tests:** skip some failing tests on the latest python versions ([9ebb6e4](https://github.com/cruzluna/sps-python/commit/9ebb6e43c193eb6e102f18c49b1898065a85541a))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([8884fda](https://github.com/cruzluna/sps-python/commit/8884fda63a2d274fb1ace1b1bc147c313bfea621))

## 0.1.0-alpha.4 (2025-06-17)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/cruzluna/sps-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** api update ([e744344](https://github.com/cruzluna/sps-python/commit/e744344e1834e68ec41e3478de7aaa81ea9efcdd))
* **api:** api update ([127d180](https://github.com/cruzluna/sps-python/commit/127d1809fae4c5a6234f9dffb4e4faf1243d3654))
* **client:** add follow_redirects request option ([294e2d0](https://github.com/cruzluna/sps-python/commit/294e2d0fc1bdc7c33604989e1117aefa0a6a3535))


### Bug Fixes

* **client:** correctly parse binary response | stream ([c31c7c8](https://github.com/cruzluna/sps-python/commit/c31c7c8614493f7b6e74c563fe8eafbe49f0d5e4))


### Chores

* **docs:** remove reference to rye shell ([620ac7b](https://github.com/cruzluna/sps-python/commit/620ac7bb94a47698679320d74dba599e04e14514))
* **tests:** add tests for httpx client instantiation & proxies ([8c4d2ce](https://github.com/cruzluna/sps-python/commit/8c4d2cea1a60eb4e21f4f900e17afe6291c76cde))
* **tests:** run tests in parallel ([9c4f91e](https://github.com/cruzluna/sps-python/commit/9c4f91ef743c3ae403c49030437742b53d7c281c))

## 0.1.0-alpha.3 (2025-05-25)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/cruzluna/sps-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** api update ([d4be406](https://github.com/cruzluna/sps-python/commit/d4be4060394cefa6861ab7d2f47a09ca73fe9e9c))
* **api:** api update ([727ef04](https://github.com/cruzluna/sps-python/commit/727ef04d5db9b2208489a13dfa65f69278c4007d))
* **api:** api update ([6ea8d2b](https://github.com/cruzluna/sps-python/commit/6ea8d2b9d6cdfb6bca702dfca43dabce1d570fdf))
* **api:** api update ([4cbaffe](https://github.com/cruzluna/sps-python/commit/4cbaffe0d38befcf8167c9910a633ad09cc8f20a))
* **api:** api update ([0ba0463](https://github.com/cruzluna/sps-python/commit/0ba046339f06112df8793862c10e8e7976e76281))
* **api:** api update ([cc10265](https://github.com/cruzluna/sps-python/commit/cc102657eb5ccedc08e62f7ac414cdb189d5f4dd))
* **api:** manual updates to openapi.stainless.yml ([a033c93](https://github.com/cruzluna/sps-python/commit/a033c935ff5ee59dc914d808324b45db44cbacfa))
* **api:** manual updates to stainless config ([39fb04e](https://github.com/cruzluna/sps-python/commit/39fb04e7847da98369b4f8f895cf1ef9c3a73463))


### Chores

* configure new SDK language ([b6faf00](https://github.com/cruzluna/sps-python/commit/b6faf005252c440af7e40e22da9498f36154548f))
* update SDK settings ([9d11cbd](https://github.com/cruzluna/sps-python/commit/9d11cbdcb5e0f10112515e48db56fea1cc9118de))
* update SDK settings ([48b1f52](https://github.com/cruzluna/sps-python/commit/48b1f52463b2de15053b7d6a4a063f87b67a3e1c))

## 0.1.0-alpha.2 (2025-05-24)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/cruzluna/sps-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** api update ([6ea8d2b](https://github.com/cruzluna/sps-python/commit/6ea8d2b9d6cdfb6bca702dfca43dabce1d570fdf))
* **api:** api update ([4cbaffe](https://github.com/cruzluna/sps-python/commit/4cbaffe0d38befcf8167c9910a633ad09cc8f20a))
* **api:** api update ([0ba0463](https://github.com/cruzluna/sps-python/commit/0ba046339f06112df8793862c10e8e7976e76281))

## 0.1.0-alpha.1 (2025-05-23)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/cruzluna/sps-python/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** api update ([cc10265](https://github.com/cruzluna/sps-python/commit/cc102657eb5ccedc08e62f7ac414cdb189d5f4dd))
* **api:** manual updates to openapi.stainless.yml ([a033c93](https://github.com/cruzluna/sps-python/commit/a033c935ff5ee59dc914d808324b45db44cbacfa))

## 0.0.1-alpha.1 (2025-05-23)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/cruzluna/sps-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* configure new SDK language ([b6faf00](https://github.com/cruzluna/sps-python/commit/b6faf005252c440af7e40e22da9498f36154548f))
* update SDK settings ([9d11cbd](https://github.com/cruzluna/sps-python/commit/9d11cbdcb5e0f10112515e48db56fea1cc9118de))
* update SDK settings ([48b1f52](https://github.com/cruzluna/sps-python/commit/48b1f52463b2de15053b7d6a4a063f87b67a3e1c))
