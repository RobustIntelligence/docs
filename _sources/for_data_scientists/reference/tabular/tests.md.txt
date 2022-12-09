Tests Configuration
===================

All of the tests RIME runs are easily configurable via a JSON configuration file.
In order to use this configuration for a run, you should specify the path to this JSON
file in the overall configuration file using the `"tests_config_path"` key.

## Global Configuration Options

This JSON file contains several global configuration options, which, if specified, will apply to all relevant tests. All of these default to `null`, which means RIME will rely on the specific test configuration to provide this value. These are:

- **`categories`**: List[str], *default* = ``[]``

    Test categories to run. Options include `Abnormal Inputs`, `Attacks`, `Bias and Fairness`, `Data Cleanliness`, `Data Poisoning Detection`, `Drift`, `Model Performance`, `Subset Performance`, and `Transformations`.

- **`run_default`**: Optional[bool], *default* = ``null``

    Whether to run default categories or not. Defaults to `True` if no `categories` are specified, `False` if any are. The default categories are `Attacks`, `Model Performance`, `Subset Performance`, and `Transformations`.
- **`global_exclude_columns`**: Optional[List[str]], *default* = `null`

    Columns to exclude from all tests.
- **`global_abnormal_inputs_performance_change_config`**: Optional[mapping], *default* = `null`

    Parameters for measuring the impact of abnormal inputs on model performance (applies to all abnormal input tests). The different values of this mapping should be:
    - `severity_thresholds`: List[float, float, float]
      
      Ascending list of three float thresholds, corresponding to the observed or simulated performance change which must be achieved in order for the test to return, respectively, Low, Medium, or High severity. This is a logical OR: if both types of performance change are measured, take the maximum of the two and return the severity corresponding to the highest threshold that was exceeded. If there are observed failing rows but the observed or simulated performance changes do not exceed any of the thresholds, return a Low severity.
    - `min_num_samples`: int 
  
      The minimum number of rows needed to reliably compute performance change. If there are fewer than this many abnormal inputs, the observed model performance change will not be taken into when determining test status and severity.

- **`global_transformation_performance_change_config`**: Optional[mapping], *default* = `null`

    Parameters for measuring the impact of transformation on model performance (applies to all transformation tests). The different values of this mapping should be:
    - `severity_thresholds`: List[float, float, float]

      Ascending list of three float thresholds, corresponding to the observed or simulated performance change which must be achieved in order for the test to return, respectively, Low, Medium, or High severity. This is a logical OR: if both types of performance change are measured, take the maximum of the two and return the severity corresponding to the highest threshold that was exceeded. If there are observed failing rows but the observed or simulated performance changes do not exceed any of the thresholds, return a Low severity.
    - `ignore_errors`: bool
    
      If False, if the model raises an error on inputs with the given abnormality then the test case will fail with High severity.
    - `num_samples_to_simulate`: int 
  
      The number of clean rows to sample and perturb for the sake of measuring the simulated performance change.

- **`global_drift_scaling_factor`**: float

    Used for drift tests. How large of an estimated change in predictions is needed to increase the Model Impact Level by 1. Defaults to `0.005`.

Besides these global parameters, there are also keys for configuration for individual tests.

## Default configuration

Below is the default configuration for all tests. A copy of this can also be found in your `rime_trial` bundle (inside the `examples/test_configs/default_test_config.json`).

```json
{
  "categories": [],
  "run_default": null,
  "custom_tests": null,
  "dynamic_configs": {},
  "numeric_outlier": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "min_normal_prop": 0.99,
    "baseline_quantile": 0.1,
    "perturb_multiplier": 1.0
  },
  "unseen_categorical": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_domain": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_email": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_url": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "rare_categories": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "include_columns": [],
    "min_num_occurrences": 0,
    "min_pct_occurrences": 0,
    "min_ratio_rel_uniform": 0.005
  },
  "out_of_range": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "std_factor": 3
  },
  "req_characters": {
    "column_specific_params": {},
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "inconsistencies": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "freq_ratio_threshold": 0.02,
    "min_correlation": 0.1,
    "max_pairwise_tests": 200,
    "max_unique_pairs_for_firewall": 15
  },
  "capitalization": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "empty_string": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "embedding_anomalies": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "distance_quantile": 0.995
  },
  "correlation_feat_drift": {
    "exclude_columns": [],
    "run": false,
    "correlation_drift_thresholds": [
      0.3,
      0.5,
      0.7
    ],
    "p_value_threshold": 0.05,
    "min_correlation": 0.1,
    "max_pairwise_tests": 200
  },
  "correlation_label_drift": {
    "exclude_columns": [],
    "run": false,
    "correlation_drift_thresholds": [
      0.3,
      0.5,
      0.7
    ],
    "p_value_threshold": 0.05
  },
  "mutual_information_feat_drift": {
    "exclude_columns": [],
    "run": false,
    "min_mutual_information": 0.1,
    "mutual_information_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_pairwise_tests": 200,
    "min_sample_size": 100
  },
  "mutual_information_label_drift": {
    "exclude_columns": [],
    "run": false,
    "mutual_information_thresholds": [
      0.1,
      0.2,
      0.3
    ]
  },
  "categorical_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ]
    }
  },
  "multiclass_pred_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ]
    }
  },
  "regression_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ],
      "num_bins": 100
    }
  },
  "categorical_drift": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "max_sample_size": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "distance_threshold": 0.2
    },
    "ignore_nans": true
  },
  "continuous_drift": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "min_num_quantiles": 1000,
      "distance_threshold": 0.2,
      "num_bins": 100
    },
    "ignore_nans": true
  },
  "prediction_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "run": true,
      "min_sample_size": 100,
      "min_num_quantiles": 1000,
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ],
      "num_bins": 100
    }
  },
  "embedding_drift": {
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "drift_statistic": "euclidean_distance",
    "params": {
      "distance_threshold": 0.1,
      "normalize": true
    }
  },
  "avg_confidence": {
    "run": true,
    "severity_thresholds": [
      0.05,
      0.1,
      0.2
    ]
  },
  "atc": {
    "run": true,
    "severity_thresholds": [
      0.05,
      0.1,
      0.2
    ]
  },
  "calibration_comparison": {
    "run": true,
    "num_bins": 10,
    "severity_level_thresholds": [
      0.02,
      0.06,
      0.1
    ]
  },
  "label_imbalance": {
    "run": false,
    "severity_thresholds": [
      0.6,
      0.75,
      0.9
    ],
    "normalize": true
  },
  "global_exclude_columns": null,
  "global_abnormal_inputs_performance_change_config": null,
  "global_transformation_performance_change_config": null,
  "out_of_range_substitution": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    },
    "std_factor": 3
  },
  "outlier_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    },
    "min_normal_prop": 0.99,
    "baseline_quantile": 0.1,
    "perturb_multiplier": 1.0
  },
  "int_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "float_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "str_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "bool_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "url_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "domain_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "email_feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "empty_string_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "req_characters_deletion": {
    "column_specific_params": {},
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "unseen_categorical_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "unseen_domain_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "unseen_email_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "unseen_url_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "null_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "capitalization_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "vulnerability": {
    "exclude_columns": [],
    "run": false,
    "severity_level_thresholds": null,
    "sample_size": 10,
    "search_count": 10
  },
  "sensitivity": {
    "exclude_columns": [],
    "run": true,
    "severity_level_thresholds": null,
    "linf_constraint": 0.01,
    "sample_size": 10
  },
  "multi_feat_vulnerability": {
    "exclude_columns": [],
    "run": false,
    "severity_level_thresholds": null,
    "l0_constraint": 3,
    "sample_size": 10,
    "search_count": 10
  },
  "multi_feat_sensitivity": {
    "exclude_columns": [],
    "run": true,
    "severity_level_thresholds": null,
    "l0_constraint": 3,
    "sample_size": 10,
    "linf_constraint": 0.01
  },
  "hopskipjump_attack": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.05,
      0.15,
      0.25
    ],
    "sample_size": 10,
    "attack_params": {
      "targeted": false,
      "norm": 2,
      "max_iter": 50,
      "max_eval": 1000,
      "init_eval": 100,
      "init_size": 100
    }
  },
  "int_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "float_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "str_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "bool_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "url_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "domain_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "email_feature_type": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "null_check": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "null_proportion": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "p_value_threshold": 0.05
  },
  "row_null_proportion": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_threshold": 0.2
    }
  },
  "required_features": {
    "run": false,
    "required_feats": null,
    "allowed_feats": null,
    "ordered": false,
    "required_only": false
  },
  "duplicate_rows": {
    "exclude_columns": [],
    "run": false
  },
  "mi_decrease_feature_to_label": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "min_mutual_information_requirement": 0.2
  },
  "high_mi_feature_to_label": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.7,
      0.8,
      0.9
    ]
  },
  "high_feature_correlation": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.7,
      0.8,
      0.9
    ],
    "max_pairwise_tests": 200,
    "min_num_samples": 100
  },
  "protected_feature_drift": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "max_sample_size": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "distance_threshold": 0.2
    },
    "ignore_nans": true
  },
  "protected_proxies": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.2,
      0.3,
      0.4
    ]
  },
  "class_imbalance": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.9,
      0.93,
      0.96
    ],
    "metric": null
  },
  "equalized_odds": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.1,
      0.2,
      0.3
    ]
  },
  "intersectional_group_fairness": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "group_fairness_avg_pred": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "group_fairness_avg_rank": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "demographic_parity": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.8,
      0.7,
      0.6
    ]
  },
  "demographic_parity_avg_pred": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.8,
      0.7,
      0.6
    ]
  },
  "demographic_parity_avg_rank": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.8,
      0.7,
      0.6
    ]
  },
  "chi_squared_independence": {
    "run": false,
    "p_value_thresholds": [
      0.005,
      0.01,
      0.05
    ],
    "min_sample_size": 100,
    "min_subset_sample_size": 20
  },
  "predict_protected_features": {
    "run": false,
    "accuracy_thresholds": [
      0.8,
      0.85,
      0.9
    ],
    "min_sample_size": 100,
    "non_protected_train_features": null,
    "max_protected_feature_cardinality": 100,
    "max_categorical_train_feature_cardinality": 100,
    "ref_data_split": 0.8
  },
  "subset_sensitivity_pos_pred": {
    "exclude_columns": [],
    "run": false,
    "performance_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "min_sample_size": 20,
    "num_samples_to_simulate": 100
  },
  "subset_sensitivity_avg_pred": {
    "exclude_columns": [],
    "run": false,
    "performance_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "min_sample_size": 20,
    "num_samples_to_simulate": 100
  },
  "subset_sensitivity_avg_rank": {
    "exclude_columns": [],
    "run": false,
    "performance_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "min_sample_size": 20,
    "num_samples_to_simulate": 100
  },
  "equal_opportunity": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "equal_opp_macro_recall": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "predictive_equality": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "exact_match_label_flipping": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.0,
      0.001,
      0.005
    ]
  }
}
```