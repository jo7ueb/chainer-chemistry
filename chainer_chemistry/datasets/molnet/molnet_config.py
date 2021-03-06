import chainer.functions as F
import chainer_chemistry
from chainer_chemistry.datasets.molnet.chembl_tasks import chembl_tasks
from chainer_chemistry.datasets.molnet.toxcast_tasks import toxcast_tasks
from chainer_chemistry.training.extensions.prc_auc_evaluator import PRCAUCEvaluator  # NOQA
from chainer_chemistry.training.extensions.roc_auc_evaluator import ROCAUCEvaluator  # NOQA

molnet_base = 'http://deepchem.io.s3-website-us-west-1.amazonaws.com/datasets/'
featurized_base = 'http://deepchem.io.s3-website-us-west-1.amazonaws.com/' \
                  + 'featurized_datasets/'


def mae(x, t):
    return chainer_chemistry.functions.mean_absolute_error(
        x, t, ignore_nan=True)


def rmse(x, t):
    mse = chainer_chemistry.functions.mean_squared_error(x, t, ignore_nan=True)
    return F.sqrt(mse)


def r2_score(x, t):
    return chainer_chemistry.functions.r2_score(x, t, ignore_nan=True)


molnet_default_config = {
    "bace_Class": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'bace.csv',
        "smiles_columns": 'mol',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "split": 'random',
        "task_type": 'classification',
        "tasks": ["Class"],
    },
    "bace_pIC50": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'bace.csv',
        "smiles_columns": 'mol',
        "metrics": {'MAE': mae},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ["pIC50"],
    },
    "bbbp": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'BBBP.csv',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "split": 'scaffold',
        "task_type": 'classification',
        "tasks": ["p_np"],
    },
    # TODO(mottodora): There are many separating ways for chembl dataset
    # TODO(mottodora): only use 5thresh dataset(sparse dataset is not used.)
    # TODO(mottodora): support mix dataset type in example
    "chembl": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'chembl_5thresh.csv.gz',
        "smiles_columns": 'smiles',
        "split": 'random',
        "task_type": 'mix',
        "tasks": chembl_tasks,
    },
    "clearance": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'clearance.csv',
        "smiles_columns": 'smile',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ["target"],
    },
    "clintox": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'clintox.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "split": 'random',
        "task_type": 'classification',
        "tasks": ["FDA_APPROVED", "CT_TOX"],
    },
    "delaney": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'delaney-processed.csv',
        "smiles_columns": 'smiles',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ['measured log solubility in mols per litre'],
    },
    "HIV": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'HIV.csv',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "split": 'scaffold',
        "task_type": 'classification',
        "tasks": ["HIV_active"],
    },
    "hopv": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'hopv.tar.gz',
        "smiles_columns": 'hopv.csv',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ['HOMO', 'LUMO', 'electrochemical_gap', 'optical_gap',
                  'PCE', 'V_OC', 'J_SC', 'fill_factor'],
    },
    "kaggle": {
        "dataset_type": 'separate_csv',
        "train_url": molnet_base + 'KAGGLE_training_'
                        'disguised_combined_full.csv.gz',
        "valid_url": molnet_base + 'KAGGLE_test1_'
                        'disguised_combined_full.csv.gz',
        "test_url": molnet_base + 'KAGGLE_test2_'
                        'disguised_combined_full.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ['3A4', 'CB1', 'DPP4', 'HIVINT', 'HIV_PROT', 'LOGD', 'METAB',
                  'NK1', 'OX1', 'OX2', 'PGP', 'PPB', 'RAT_F', 'TDI', 'THROMBIN'
                  ]
    },

    "lipo": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'Lipophilicity.csv',
        "smiles_columns": 'smiles',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ['exp'],
    },
    "muv": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'muv.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'prc_auc': PRCAUCEvaluator},
        "split": 'random',
        "task_type": 'classification',
        "tasks": ['MUV-692', 'MUV-689', 'MUV-846', 'MUV-859', 'MUV-644',
                  'MUV-548', 'MUV-852', 'MUV-600', 'MUV-810', 'MUV-712',
                  'MUV-737', 'MUV-858', 'MUV-713', 'MUV-733', 'MUV-652',
                  'MUV-466', 'MUV-832'],
    },
    "nci": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'nci_unique.csv',
        "smiles_columns": 'smiles',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ['CCRF-CEM', 'HL-60(TB)', 'K-562', 'MOLT-4', 'RPMI-8226',
                  'SR', 'A549/ATCC', 'EKVX', 'HOP-62', 'HOP-92', 'NCI-H226',
                  'NCI-H23', 'NCI-H322M', 'NCI-H460', 'NCI-H522', 'COLO 205',
                  'HCC-2998', 'HCT-116', 'HCT-15', 'HT29', 'KM12', 'SW-620',
                  'SF-268', 'SF-295', 'SF-539', 'SNB-19', 'SNB-75', 'U251',
                  'LOX IMVI', 'MALME-3M', 'M14', 'MDA-MB-435', 'SK-MEL-2',
                  'SK-MEL-28', 'SK-MEL-5', 'UACC-257', 'UACC-62', 'IGR-OV1',
                  'OVCAR-3', 'OVCAR-4', 'OVCAR-5', 'OVCAR-8', 'NCI/ADR-RES',
                  'SK-OV-3', '786-0', 'A498', 'ACHN', 'CAKI-1', 'RXF 393',
                  'SN12C', 'TK-10', 'UO-31', 'PC-3', 'DU-145', 'MCF7',
                  'MDA-MB-231/ATCC', 'MDA-MB-468', 'HS 578T', 'BT-549', 'T-47D'
                  ]
    },
    "pcba": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'pcba.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'prc_auc': PRCAUCEvaluator},
        "split": 'random',
        "task_type": 'classification',
        "tasks":
            ['PCBA-1030', 'PCBA-1379', 'PCBA-1452', 'PCBA-1454', 'PCBA-1457',
             'PCBA-1458', 'PCBA-1460', 'PCBA-1461', 'PCBA-1468', 'PCBA-1469',
             'PCBA-1471', 'PCBA-1479', 'PCBA-1631', 'PCBA-1634', 'PCBA-1688',
             'PCBA-1721', 'PCBA-2100', 'PCBA-2101', 'PCBA-2147', 'PCBA-2242',
             'PCBA-2326', 'PCBA-2451', 'PCBA-2517', 'PCBA-2528', 'PCBA-2546',
             'PCBA-2549', 'PCBA-2551', 'PCBA-2662', 'PCBA-2675', 'PCBA-2676',
             'PCBA-411', 'PCBA-463254', 'PCBA-485281', 'PCBA-485290',
             'PCBA-485294', 'PCBA-485297', 'PCBA-485313', 'PCBA-485314',
             'PCBA-485341', 'PCBA-485349', 'PCBA-485353', 'PCBA-485360',
             'PCBA-485364', 'PCBA-485367', 'PCBA-492947', 'PCBA-493208',
             'PCBA-504327', 'PCBA-504332', 'PCBA-504333', 'PCBA-504339',
             'PCBA-504444', 'PCBA-504466', 'PCBA-504467', 'PCBA-504706',
             'PCBA-504842', 'PCBA-504845', 'PCBA-504847', 'PCBA-504891',
             'PCBA-540276', 'PCBA-540317', 'PCBA-588342', 'PCBA-588453',
             'PCBA-588456', 'PCBA-588579', 'PCBA-588590', 'PCBA-588591',
             'PCBA-588795', 'PCBA-588855', 'PCBA-602179', 'PCBA-602233',
             'PCBA-602310', 'PCBA-602313', 'PCBA-602332', 'PCBA-624170',
             'PCBA-624171', 'PCBA-624173', 'PCBA-624202', 'PCBA-624246',
             'PCBA-624287', 'PCBA-624288', 'PCBA-624291', 'PCBA-624296',
             'PCBA-624297', 'PCBA-624417', 'PCBA-651635', 'PCBA-651644',
             'PCBA-651768', 'PCBA-651965', 'PCBA-652025', 'PCBA-652104',
             'PCBA-652105', 'PCBA-652106', 'PCBA-686970', 'PCBA-686978',
             'PCBA-686979', 'PCBA-720504', 'PCBA-720532', 'PCBA-720542',
             'PCBA-720551', 'PCBA-720553', 'PCBA-720579', 'PCBA-720580',
             'PCBA-720707', 'PCBA-720708', 'PCBA-720709', 'PCBA-720711',
             'PCBA-743255', 'PCBA-743266', 'PCBA-875', 'PCBA-881', 'PCBA-883',
             'PCBA-884', 'PCBA-885', 'PCBA-887', 'PCBA-891', 'PCBA-899',
             'PCBA-902', 'PCBA-903', 'PCBA-904', 'PCBA-912', 'PCBA-914',
             'PCBA-915', 'PCBA-924', 'PCBA-925', 'PCBA-926', 'PCBA-927',
             'PCBA-938', 'PCBA-995'],
    },
    "pdbbind_smiles": {
        "subset": ["core", "full", "refined"],
        "dataset_type": 'one_file_csv',
        "url": {'core': molnet_base + 'core_smiles_labels.csv',
                'full': molnet_base + 'full_smiles_labels.csv',
                'refined': molnet_base + 'refined_smiles_labels.csv'},
        "smiles_columns": 'smiles',
        "metrics": {'R2': r2_score},
        "split": 'time',
        "task_type": 'regression',
        "tasks": ["-logKd/Ki"],
    },
    "pdbbind_grid": {
        "pdbbind_subset": ["core", "full", "refined"],
        "dataset_type": 'joblib',
        "url": {'core': featurized_base + 'core_grid.tar.gz',
                'full': featurized_base + 'full_grid.tar.gz',
                'refined': featurized_base + 'refined_grid.tar.gz'},
        "smiles_columns": '',
        "metrics": {'R2': r2_score},
        "split": 'time',
        "task_type": 'regression',
        "tasks": ["-logKd/Ki"],
    },
    "ppb": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'PPB.csv',
        "smiles_columns": 'smiles',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ["exp"],
    },
    # TODO(motoki): there are multiple data types in qm7 dataset.
    "qm7": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'qm7.csv',
        "smiles_columns": 'smiles',
        "metrics": {'MAE': mae},
        "split": 'stratified',
        "task_type": 'regression',
        "tasks": ["u0_atom"],
    },
    # TODO(motoki): there are sdf data types in qm8 dataset.
    "qm8": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'qm8.csv',
        "smiles_columns": 'smiles',
        "metrics": {'MAE': mae},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ["E1-CC2", "E2-CC2", "f1-CC2", "f2-CC2", "E1-PBE0", "E2-PBE0",
                  "f1-PBE0", "f2-PBE0", "E1-PBE0", "E2-PBE0", "f1-PBE0",
                  "f2-PBE0", "E1-CAM", "E2-CAM", "f1-CAM", "f2-CAM"],
    },
    # TODO(motoki): there are sdf data types in qm9 dataset.
    "qm9": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'qm9.csv',
        "smiles_columns": 'smiles',
        "metrics": {'MAE': mae},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ["mu", "alpha", "homo", "lumo", "gap", "r2", "zpve", "cv",
                  "u0", "u298", "h298", "g298"],
    },
    "SAMPL": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'SAMPL.csv',
        "smiles_columns": 'smiles',
        "metrics": {'RMSE': rmse},
        "split": 'random',
        "task_type": 'regression',
        "tasks": ["expt"],
    },
    "sider": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'sider.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "split": 'random',
        "task_type": 'classification',
        "tasks": ['Hepatobiliary disorders',
                  'Metabolism and nutrition disorders', 'Product issues',
                  'Eye disorders', 'Investigations',
                  'Musculoskeletal and connective tissue disorders',
                  'Gastrointestinal disorders', 'Social circumstances',
                  'Immune system disorders',
                  'Reproductive system and breast disorders',
                  'Neoplasms benign, malignant and unspecified '
                  '(incl cysts and polyps)',
                  'General disorders and administration site conditions',
                  'Endocrine disorders', 'Surgical and medical procedures',
                  'Vascular disorders', 'Blood and lymphatic system disorders',
                  'Skin and subcutaneous tissue disorders',
                  'Congenital, familial and genetic disorders',
                  'Infections and infestations',
                  'Respiratory, thoracic and mediastinal disorders',
                  'Psychiatric disorders', 'Renal and urinary disorders',
                  'Pregnancy, puerperium and perinatal conditions',
                  'Ear and labyrinth disorders', 'Cardiac disorders',
                  'Nervous system disorders',
                  'Injury, poisoning and procedural complications'],
    },
    "tox21": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'tox21.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "split": 'random',
        "task_type": 'classification',
        "tasks": ['NR-AR', 'NR-AR-LBD', 'NR-AhR', 'NR-Aromatase', 'NR-ER',
                  'NR-ER-LBD', 'NR-PPAR-gamma', 'SR-ARE', 'SR-ATAD5', 'SR-HSE',
                  'SR-MMP', 'SR-p53'],
    },
    "toxcast": {
        "dataset_type": 'one_file_csv',
        "url": molnet_base + 'toxcast_data.csv.gz',
        "smiles_columns": 'smiles',
        "metrics": {'binary_accuracy': F.binary_accuracy,
                    'roc_auc': ROCAUCEvaluator},
        "loss": F.sigmoid_cross_entropy,
        "split": 'random',
        "task_type": 'classification',
        "tasks": toxcast_tasks,
    },
}
