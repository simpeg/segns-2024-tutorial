import numpy as np
import re

def parse_gex_file(fname):
    # build up a dictionary of details
    loop_points = []
    hm_wave = []
    lm_wave = []
    gate_times = []
    current_section = None
    general_info = {}
    channel_info = []
    channel_ids = []
    with open(fname, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            if "[General]" in line:
                current_section = "General"
                info = general_info
            elif "[Channel" in line:
                current_section = "Channel"
                id_search = re.search("\d+", line).span()
                channel_id = int(line[id_search[0]:id_search[1]])
                if channel_id not in channel_ids:
                    channel_ids.append(channel_id)
                    channel_info.append({})
                info = channel_info[channel_id-1]
            line = line.split("=")
            if len(line)==2:
                description, data = line
                try:
                    data = np.asarray(data.split(), dtype=float)
                    if len(data) == 1:
                        data = data[0]
                    if int(data) == data:
                        data = int(data)
                except:
                    pass

                if (match:= re.search("TxLoopPoint", description)) is not None:
                    # The Tx points will always be listed in order
                    loop_points.append(data)
                elif (match:= re.search("Waveform\w+Point\d+", description)) is not None:
                    if "LM" in description:
                        lm_wave.append(data)
                    if "HM" in description:
                        hm_wave.append(data)
                elif (match:= re.search("GateTime\d+", description)) is not None:
                    gate_times.append(data)
                else:
                    try:
                        data = np.asarray(data.split(), dtype=float)
                        if len(data) == 1:
                            data = data[0]
                    except:
                        pass
                    info[description] = data

    general_info['TxLoopPoints'] = np.asarray(loop_points)
    hm_wave = np.asarray(hm_wave)
    waveforms = {}
    if len(hm_wave) > 0:
        wave = {'time':hm_wave[:, 0], 'form':hm_wave[:, 1]}
        waveforms['HM'] = wave
    lm_wave = np.asarray(lm_wave)
    if len(lm_wave) > 0:
        wave = {'time':lm_wave[:, 0], 'form':lm_wave[:, 1]}
        waveforms['LM'] = wave
    general_info['Waveforms'] = waveforms
    gate_times = np.asarray(gate_times)
    if len(gate_times) > 0:
        times = {}
        times['start'] = gate_times[:, 1]
        times['end'] = gate_times[:, 2]
        times['center'] = gate_times[:, 0]
        general_info['GateTimes'] = times
    info = {}
    info["General"] = general_info
    for channel in channel_ids:
        info[f"Channel{channel}"] = channel_info[channel-1]
    return info