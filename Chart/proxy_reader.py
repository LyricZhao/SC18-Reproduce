def read_result(file_name):
    result = {
            'flops': 0,
            'time': 0
    }
    with open(file_name, 'r') as f:
        for raw_line in f.read().split('\n'):
            if raw_line.find('time for') > -1:
                result['time'] = float(raw_line[raw_line.find(': '):])
            elif raw_line.find('GFLOPS (hardware)') > -1:
                result['flops'] = float(raw_line[raw_line.find(': '):])
    return result
