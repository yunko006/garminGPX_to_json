from pathlib import Path
import json


def create_nested_dict(*datas:str) -> dict:
    """
    Take  *args and turn them into a nested dict such as : {"data[0]: {}, "data[1]: {}, etc"}
    Parameters : 
        *datas: args str
    Returns : 
        data_dict : a nested dict
    """
    data_dict = { data : {} for data in datas }
    return data_dict


def clean_line(line: str, suffix: str) -> str:
    """
    Clean a line from the tcx file.

    Parameters : 
            line: A line from the file.
            suffix : The suffix from the line we need to remove.
    
    Returns: 
            line_without_suffix: a str who matches our needs.
    """
    striped_line = line.rstrip().lstrip()
    line_without_suffix = striped_line.replace(f'<{suffix}>', "").replace(f'</{suffix}>', "")

    return line_without_suffix


def append_data_to_dict(data_dict: dict, path:Path) -> dict:
    """
    Append each line to its nested dict
    """
    # met sous forme de list les valeurs keys du dict.
    datas = [k for k in data_dict.keys()]

    with open(path) as f:
        for line in f:
            for data in datas:
                if f"<{data}>" in line:
                    data_dict[data][len(data_dict[data])] = clean_line(line, data)

    
    return data_dict

 
def dict_to_json_file(d: dict, path:str,   n:int =4) -> None:
    """Convert a dict to a json str and then write it to a new file."""

    new_file = Path(f"{path.stem}.json")
    # print(new_file.exists())

    if not new_file.exists():
        new_file.touch()
        json_dict = json.dumps(d, indent=n)
        new_file.write_text(json_dict)
        print("fichier bien créé.")
        return 0   

    else:
        print("fichier existe deja.")
        return -1


def main() ->None:
    """
    Main function of this script.
    """
    #path = str(input('Path du fichier: '))
    activity_path = Path('activity_7787466259.json')
    # create base dict
    base_dict = create_nested_dict('Time', 'LatitudeDegrees', 'LongitudeDegrees', 'AltitudeMeters', 'DistanceMeters', 'ns3:Speed', 'ns3:RunCadence' )
    # append value to base dict
    data_dict = append_data_to_dict(base_dict, activity_path)
    # convert base_dict to a new json file
    dict_to_json_file(data_dict, activity_path)
 

if __name__ == "__main__":
    main()
