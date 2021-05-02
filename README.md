<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Chrono4/NovoLS">
    <img src="images/novols.jpg" alt="Logo" width="216" height="121">
  </a>

  <h3 align="center">MILES</h3>

  <p align="center">
    MultIlingual LExical Simplifier
    <br />
    <a href="https://github.com/Kvasirs/MILES"><inspectistrong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://arxiv.org/abs/2006.14939">Read LSBert Paper</a>
    ·
    <a href="https://github.com/Kvasirs/MILES/issues">Report Bug</a>
    ·
    <a href="https://github.com/Kvasirs/MILES/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

MILES is a multilingual text simplifier inspired by LSBert - A lexical simplification approach proposed by Qiang et al. in 2018. Unlike LSBert, MiLeS makes use of the bert-base-multilingual-uncased model, as well as language-agnostic approaches to complex word identification (CWI) and candidate ranking.

### Language Support

MILES currently supports 22 languages:

* Arabic
* Bulgarian
* Catalan
* Czech
* Danish
* Dutch
* English
* Finnish
* French
* German
* Hungarian
* Indonesian
* Italian
* Norwegian
* Polish
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish
* Ukranian

### Prerequisites

* [Hugginface Transformers](https://huggingface.co/transformers/)

* [Gensim](https://radimrehurek.com/gensim/)

* [NLTK](https://www.nltk.org/)

* [Wordfreq](https://pypi.org/project/wordfreq/)

* [Stop Words](https://pypi.org/project/stop-words/)

* [PyTorch](https://pytorch.org/)

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Installation

1. Clone the repo
```sh
git clone https://https://github.com/Chrono4/NovoLS.git
```

2. Run generation script within resources/embeddings to generate vector model
  ```sh
  python gen_keyed_vectors.py <glove vector path>
  ```

3. Run simplifier.py
```sh
python simplifier.py
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://https://github.com/Chrono4/NovoLS/issues) for a list of proposed features (and known issues).

<!-- CONTACT -->
## Contact

If you have any questions or concerns, message me on [LinkedIn](https://www.linkedin.com/in/kane-miles-dev/) or email me at Kanemiles445@gmail.com.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Shout out to Prof. Dr. Goran Glavaš for answering questions I had about the project. My dissertation would not have been what it was without his help. For those interested, a minimal version of Prof. Glavaš and Štajner's LightLS system can be found [here](https://github.com/codogogo/lightls)
