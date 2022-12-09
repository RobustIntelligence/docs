# Custom embeddings

Data science often makes use of an extremely high number of dimensions to perform
mathematical transformations as part of the analysis of a data set. When these
dimensions don't provide useful information without their adjacent contexts, an
embedding provides a way to attempt a holistic analysis by grouping similar dimensions.

You can specify the particular embeddings used by your model and make them available to
the RI Platform by using the Python SDK.

## NLP custom embedding example

This example uses a custom configuration to define the embedding used by the model and then references the loading function as normal.

The NLP custom configuration JSON object:

```
{
  "run_name": "ArXiv ( With Model )",
  "data_info": {
    "ref_path": "test_data/data/nlp/classification/arxiv-small-train.json",
    "eval_path": "test_data/data/nlp/classification/arxiv-small-val.json",
    "embeddings": [
      {
        "key": "sentence_embedding"
      }
    ]
  },
  "model_info": {
    "path": "test_data/models/nlp/classification/model.py"
  },
  "model_task": "Text Classification",
  "random_seed": 42,
  "silent_errors": false,
  "tests_config_path": "test_data/configs/nlp/classification/test_config.json"
}
```

The data relating to that configuration:

```
[
  {
    "timestamp": "2007-06-12 23:12:00",
    "text": "Variations on Kaluza-Klein Cosmology",
    "sentence_embedding": [
      -1.011288046836853,
      0.4852420687675476,
      -3.2986080646514893,
      -1.771178960800171,
      -0.5122381448745728,
      -0.4211215376853943,
      -0.5741060972213745,
      1.1818445920944214,
      -0.5698719024658203,
      -0.95805424451828,
      1.6936663389205933,
      -0.4567836821079254,
      -0.4774229824542999,
      0.5969648361206055,
      0.6787158250808716,
      -0.9607284069061279,
      -0.2594589293003082,
      -0.38474351167678833,
      -1.2812590599060059,
      -0.6660887598991394
    ]
  },
  {
    "timestamp": "2007-06-12 23:12:00",
    "text": "Negative Energy Densities in Extended Sources Generating Closed Timelike\n  Curves in General Relativity with and without Torsion",
    "sentence_embedding": [
      -0.2336328625679016,
      -0.007996942847967148,
      -3.97566819190979,
```

## Tabular custom embedding example

For tabular data, an example embedding is defined by the following JSON:

```
{
  ...
  "data_info": {
    ...
    "embeddings": [{"name": "foobar": "cols": ["colX", "colY", "colZ"]}]
  }
}
```

The dataset must include the specified columns `colX`, `colY`, and `colZ`.
