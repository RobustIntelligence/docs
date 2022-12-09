### Image Classification Testing Config


Below is the default configuration for all Image Classification tests. A copy of this can also be found in your `rime_trial` bundle (inside the `images_examples/classification/default_test_config.json`).

```python
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
  "global_sample_size": null,
  "metadata_tests": null,
  "gaussian_blur": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "kernel_size": [
      19,
      19
    ],
    "sigma": 5
  },
  "color_jitter": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "brightness": 0.1,
    "contrast": 0.1,
    "saturation": 0.1,
    "hue": 0.1
  },
  "gaussian_noise": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.01,
      0.1,
      0.25
    ],
    "mean": 0,
    "sigma": 0.03
  },
  "vertical_flip": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ]
  },
  "horizontal_flip": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ]
  },
  "randomize_pixels_with_mask": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "probability": 0.1
  },
  "contrast_increase": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "percent": 0.5
  },
  "contrast_decrease": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "percent": 0.5
  },
  "add_rain": {
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "alpha": 0.5,
    "transformation_type": "Add Rain"
  },
  "add_snow": {
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "alpha": 0.5,
    "transformation_type": "Add Snow"
  },
  "hopskipjump_attack": {
    "run": false,
    "sample_size": 5,
    "severity_thresholds": [
      0.1,
      0.05,
      0.01
    ],
    "attack_params": {
      "targeted": false,
      "norm": 2,
      "max_iter": 30,
      "max_eval": 50,
      "init_eval": 20,
      "init_size": 20
    }
  },
  "square_attack": {
    "run": false,
    "sample_size": 5,
    "severity_thresholds": [
      0.1,
      0.25,
      0.5
    ],
    "attack_params": {
      "norm": "inf",
      "max_iter": 100,
      "eps": 0.02,
      "p_init": 0.25,
      "nb_restarts": 5,
      "square": true
    }
  },
  "exact_match_label_flipping": {
    "run": false,
    "severity_thresholds": [
      0.0,
      0.001,
      0.005
    ]
  }
}
```