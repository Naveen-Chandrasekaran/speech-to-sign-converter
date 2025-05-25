<h1 align="center">👋 Sign Translate</h1>


<hr>

## Key Features

### [Sign Language Production](https://github.com/sign/translate/wiki/Spoken-to-Signed)

```
┌─────────────────────┐
│Spoken Language Audio│                                                              ┌─────────┐
└─────────┬───────────┘                                                  ┌──────────►│Human GAN│
          │                                                              │           └─────────┘
          ▼                                                              │
┌────────────────────┐     ┌───────────────┐     ┌───────────┐    ┌──────┴──────┐    ┌───────────────┐
│Spoken Language Text├────►│Normalized Text├────►│SignWriting├───►│Pose Sequence├───►│Skeleton Viewer│
└─────────┬──────────┘     └───────────────┘     └───────────┘    └──────┬──────┘    └───────────────┘
          │                        ▲                   ▲                 │
          ▼                        │                   │                 │           ┌─────────┐
┌───────────────────────┐          │                   │                 └──────────►│3D Avatar│
│Language Identification├──────────┘───────────────────┘                             └─────────┘
└───────────────────────┘
```

### [Sign Language Translation](https://github.com/sign/translate/wiki/Signed-to-Spoken)

```
┌──────────────────────────┐                                ┌────────────────────┐
│Upload Sign Language Video│                      ┌────────►│Spoken Language Text│
└──────────┬───────────────┘                      │         └──────────┬─────────┘
           │                                      │                    │
           │          ┌────────────┐       ┌──────┴────┐               │
           ├─────────►│Segmentation├──────►│SignWriting│               │
           │          └────────────┘       └───────────┘               │
           │                                                           ▼
┌──────────┴────────────────┐                               ┌─────────────────────┐
│Camera Sign Language Video │                               │Spoken Language Audio│
└───────────────────────────┘                               └─────────────────────┘
```

### Want to Help?

Join us on the journey to revolutionize sign language communication.
Follow our progress on the [Project Board][project-board],
shape the project's future,
and delve deeper into our vision and plans in the [Wiki][wiki].

Wish to report a bug, contribute some code, or enhance documentation? Fantastic!
Check our guidelines for [contributing][contributing] and then explore our issues marked as <kbd>[help wanted](https://github.com/sign/translate/labels/help%20wanted)</kbd> or <kbd>[good first issue](https://github.com/sign/translate/labels/good%20first%20issue)</kbd>.

**Find this useful? Give our repo a star :star: :arrow_up:.**

[![Stargazers repo roster for @sign/translate](https://reporoster.com/stars/sign/translate)](https://github.com/sign/translate/stargazers)

[wiki]: https://github.com/sign/translate/wiki/Spoken-to-Signed
[contributing]: https://github.com/sign/.github/blob/main/CONTRIBUTING.md
[project-board]: https://github.com/sign/translate/projects/1

## Development

### Prerequisites

- Install [Node.js] which includes [Node Package Manager][npm]

### Setting Up the Project

Install dependencies locally:

```bash
npm install
```

Run the application:

```bash
npm start
```

Test the application:

```bash
npm test
```

Run the application on iOS:

```bash
npm run build:full && \
npx cap sync ios && \
npx cap run ios
```

[node.js]: https://nodejs.org/
[npm]: https://www.npmjs.com/get-npm

### Cite

```bibtex
@misc{moryossef2023signmt,
    title={sign.mt: Effortless Real-Time Sign Language Translation},
    author={Moryossef, Amit},
    howpublished={\url{https://sign.mt/}},
    year={2023}
}
```
