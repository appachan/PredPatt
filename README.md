PredPatt: Predicate-Argument Extraction from Universal Dependencies
===================================================================

We present PredPatt, a framework of extensible, interpretable, language-neutral
predicate-argument extraction patterns. PredPatt bridges the deep syntax of the
Universal Dependency project to an initial shallow semantic layer: this can form
the basis for future layering of semantic annotations atop
[Universal Dependency](http://universaldependencies.org/) treebanks, and
separately can be considered a linguistically well-founded component of a
"Universal IE" mechanism.

<!--
We consider these dual-uses through manual evaluation of output based on
automatically generated parses in English, and on gold treebanks in Chinese,
English, Hebrew, Hindi, and Spanish.
-->

PredPatt is part of a wider initiative on
[decompositional semantics](http://decomp.net) at Johns Hopkins University. To
that end, it has been used to bootstrap semantic annotations in our recent EMNLP
2016 paper ([White et al., 2016](doc/references.md)).

PredPatt shows the best precision and recall when compared with several prominent 
Open IE tools on a large benchmark
([Zhang et al., 2017](http://www.cs.jhu.edu/~s.zhang/assets/pdf/iwcs17.pdf)).


> PredPatt extracts predicates and arguments from text .

    ?a extracts ?b from ?c
        ?a: PredPatt
        ?b: predicates
        ?c: text
    ?a extracts ?b from ?c
        ?a: PredPatt
        ?b: arguments
        ?c: text


## Table of contents

* [Get started](doc/get-started.md) (See our new [tutorial](tutorial.ipynb) for programmatic usage.)
* [Motivation](doc/intro-and-motivation.md)
* Sample output:
  - Documentation tests: [English](doc/DOCTEST.md)
  - UD Bank: [English](test/data.100.fine.all.ud.expect), [Portuguese](test/pt.dev.conllu.expect), and [Spanish](test/es.dev.conllu.expect).
  - Selected examples: [Chinese](doc/chinese.md), [Portuguese](doc/portuguese.md), [Spanish](doc/spanish.md)
* How PredPatt works: [high-level overview](doc/high-level-overview.md), [detailed list of rules](doc/RULES.md)
* [Evaluation](doc/evaluation.md)
* [Related work](doc/related-work.md)
* [References](doc/references.md)



<!--
## PredPatt: Predicate-Argument Extraction from Universal Dependencies

PredPatt is a framework of extensible, interpretable, language-neutral
predicate-argument extraction patterns. PredPatt bridges the deep syntax of the
[Universal Dependency](http://universaldependencies.org/) project to an initial
shallow semantic layer: this can form the basis for future layering of semantic
annotations atop Universal Dependency treebanks, and separately can be
considered a linguistically well-founded component of a "Universal IE"
mechanism.

> PredPatt extracts predicates and arguments from text .

    ?a extracts ?b from ?c
        ?a: PredPatt
        ?b: predicates
        ?c: text
    ?a extracts ?b from ?c
        ?a: PredPatt
        ?b: arguments
        ?c: text

See [doctests](doc/DOCTEST.md) for sample output (as well as,
[Portuguese](doc/portuguese.md), [Spanish](doc/spanish.md),
[Chinese](doc/chinese.md)). Additionally, we have example output from the
UDBank in [English](test/data.100.fine.all.ud.expect),
[Spanish](test/es.dev.conllu.expect), and
[Portuguese](test/pt.dev.conllu.expect).
-->

## Citation

If you use PredPatt please cite it as follows.

    @InProceedings{zhang-EtAl:2017:IWCS,
        author = {Zhang, Sheng and Rudinger, Rachel and {Van Durme}, Ben },
        title = {{An Evaluation of PredPatt and Open IE via Stage 1 Semantic Role Labeling}},
        booktitle = {Proceedings of the 12th International Conference on Computational Semantics (IWCS)},
        month = {September},
        year = {2017},
        address = {Montpellier, France}
    }

    @InProceedings{white-EtAl:2016:EMNLP2016,
        author    = {White, Aaron Steven  and  Reisinger, Drew  and  Sakaguchi, Keisuke  and  Vieira, Tim  and  Zhang, Sheng  and  Rudinger, Rachel  and  Rawlins, Kyle  and  {Van Durme}, Benjamin},
        title     = {{Universal Decompositional Semantics on Universal Dependencies}},
        booktitle = {Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing},
        month     = {November},
        year      = {2016},
        address   = {Austin, Texas},
        publisher = {Association for Computational Linguistics},
        pages     = {1713--1723},
        url       = {https://aclweb.org/anthology/D16-1177}
    }

## License

[BSD](LICENSE)
