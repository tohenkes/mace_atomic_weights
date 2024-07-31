import subprocess

name = 'atomic_weights_test'
train_file = 'train_weights.xyz'
valid_fraction = 0.05
test_file = 'test.xyz'
config_type_weights = "{\"Default\": 1.0}"
E0s = 'average'
model = 'MACE'
hidden_irreps = '16x0e + 16x1o'
r_max = 3.0
batch_size = 5
max_num_epochs = 5
swa = False
start_swa = 10
ema = True
ema_decay = 0.99
amsgrad = True
restart_latest = True
device = 'cuda'
loss_fn ="atomic_weighted_energy_forces" #'weighted'
energy_key = 'energy'
forces_key = 'forces'
stress_key = 'stress'
default_dtype = 'float32'

pythonpath = '/home/thenkes/Documents/Uni/Promotion/Research/atomic_weighted_mace'

command = f'mace_run_train ' \
          f'--name={name} ' \
          f'--train_file="{train_file}" ' \
          f'--valid_fraction={valid_fraction} ' \
          f'--test_file="{test_file}" ' \
          f'--config_type_weights="{config_type_weights}" ' \
          f'--E0s={E0s} ' \
          f'--model="{model}" ' \
          f'--hidden_irreps="{hidden_irreps}" ' \
          f'--r_max={r_max} ' \
          f'--batch_size={batch_size} ' \
          f'--max_num_epochs={max_num_epochs} ' \
          f'--swa ' \
          f'--start_swa={start_swa} ' \
          f'--ema ' \
          f'--ema_decay={ema_decay} ' \
          f'--amsgrad ' \
          f'--restart_latest ' \
          f'--device={device} ' \
          f'--loss="{loss_fn}" ' \
        f'--energy_key={energy_key} ' \
        f'--forces_key={forces_key} ' \
        f'--stress_key={stress_key} ' \
        f'--default_dtype={default_dtype} '

subprocess.run(f'export PYTHONPATH={pythonpath}', shell=True)
subprocess.run(command, shell=True)

