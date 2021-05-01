<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Chrono4/NovoLS">
    <img src="images/novols.jpg" alt="Logo" width="216" height="121">
  </a>

  <h3 align="center">NovoLS</h3>

  <p align="center">
    An unsupervised text simplification system.
    <br />
    <a href="https://github.com/Chrono4/NovoLS"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.academia.edu/43532843/NovoLS_A_Lexical_Text_Simplification_Web_Service?source=swp_share">Read Thesis</a>
    ·
    <a href="https://github.com/Chrono4/NovoLS/issues">Report Bug</a>
    ·
    <a href="https://github.com/Chrono4/NovoLS/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

NovoLS is a lexical text simplification system which I constructed as part of my dissertation project. It is largely insipired by LightLS — an older lexcial text simplifier proposed by Prof. Dr. Goran Glavaš and Dr. Sanja Štajner in 2015. Both NovoLS and LightLS make use of GloVe word embeddings to find ‬simplification candidates for complex words, which are then ranked on a number of different features. My thesis can be found [here](https://www.academia.edu/43532843/NovoLS_A_Lexical_Text_Simplification_Web_Service?source=swp_share).

### Prerequisites

* [Gensim](https://radimrehurek.com/gensim/)

* [NLTK](https://www.nltk.org/)

* [Wordfreq](https://pypi.org/project/wordfreq/)

* [Wikipedia 2014 + Gigaword 5 GloVe Embeddings](https://nlp.stanford.edu/projects/glove/)
<br><b>Note - </b> After downloading glove.6B.zip, we used the 300d embeddings, however, any of the packaged embeddings can be used.

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
