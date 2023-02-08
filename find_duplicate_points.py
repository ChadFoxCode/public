


def get_duplicate_points(translation_array = None,
                         rotation_array = None,
                         tolerance = 0.0,
                         ):

    '''
    get_duplicate_points(translation_array = None, rotation_array = None, tolerance = 0.0) 
    
      compares and returns indices / Point ID's with the same transform values within a provided tolerance

      get_duplicate_points can find: 

        - Indices (Point IDs) with duplicate translation values,
        OR
        - Indices (Point IDs) with duplicate rotation values 
        OR 
        - When providing translation and rotation arrays of values, it will compare and return indices where 2 or more indices 
          exist in both a set translation duplicate indices and rotation duplicate indices. 
          
    :param: translation_array = None  - expects a list of arrays of position values, tuple, list, set, etc. eg  [(123.45, 100.1, -9000.1, ...), ...]
    :param: translation_array = None  - expects a list of arrays of orintation values, tuple, list, set, etc. eg  [(180.45, 360.1, -90.1, ...), ...]
    :param: tolerance = 0.0           - Default 0 tolerance, the search for duplicates will return values that are within this tolerance. definitely 
                                        has a margin of error and better logic would be needed to find clusters of poitns that all fall within the 
                                        tolerance. Hmmm
     '''
    
    #todo impliment tolerance feature. Might be optimal for speed to use rounding decimal values vs numerical comparison?

    t_duplicate_dict = {}
    r_duplicate_dict = {}

    print(translation_array, rotation_array)
    # Compare translation values and store indices for values that match 1 or more times.
    if translation_array:
        t_compare = {}
        for i, tup in enumerate(translation_array):
            if tup in t_compare:
                if tup not in t_duplicate_dict:
                    t_duplicate_dict[tup] = [i]
                else:
                    t_duplicate_dict[tup].append(i)

                compare_i = t_compare[tup]

                if compare_i not in t_duplicate_dict[tup]:
                    t_duplicate_dict[tup].append(compare_i)
            else:
                t_compare[tup] = i
        t_duplicate_indices = [i for i in t_duplicate_dict.values()]

    # Compare rotation values and store indices for values that match 1 or more times.
    if rotation_array:
        r_compare = {}
        r_duplicate_dict = {}
        for i, tup in enumerate(rotation_array):
            if tup in r_compare:
                if tup not in r_duplicate_dict:
                    r_duplicate_dict[tup] = [i]
                else:
                    r_duplicate_dict[tup].append(i)

                compare_i = r_compare[tup]

                if compare_i not in r_duplicate_dict[tup]:
                    r_duplicate_dict[tup].append(compare_i)
            else:
                r_compare[tup] = i
        r_duplicate_indices = [i for i in r_duplicate_dict.values()]


    # QC printouts --
    print(r_duplicate_dict)
    print(t_duplicate_dict)
    print(len(r_duplicate_dict), len(t_duplicate_dict))

    if translation_array and not rotation_array:
        return t_duplicate_indices
    elif rotation_array and not translation_array:
        return r_duplicate_indices
    elif translation_array and rotation_array:
        duplicate_rt = []
        for t_index_list in t_duplicate_indices:
            for r_index_list in r_duplicate_indices:
                match = set(t_index_list) & set(r_index_list)
                if len(match) >= 2:
                    duplicate_rt.append(tuple(match))


        print(len(duplicate_rt))
        print(duplicate_rt)

        return duplicate_rt

# run test when py file executed
if __name__ == "__main__":

  # example transform array
  t = [(123.45, 100.1, -9000.1, 42.0),
       (123.45, 100.1, -9000.1, 42.0),
       (658.5,-852.852,97.64,31.01),
       (36.336,-8791.0,658.785,1608.222),
       (123.45, 100.1, -9000.1, 42.0),
       (658.5, -852.852, 97.64, 31.01)
       ]
  # example rotation array
  r = [(333.33,222.22,-111.11,777.77777),
       (333.33,222.22,-111.11,777.77777),
       (888.5,-777.852,999.64,222.01),
       (2.336,-2782.0,792.785,44.222),
       (333.33,222.22,-111.11,777.77777),
       (888.5,-777.852,999.64,222.01)
       ]

  get_duplicate_points(t, r)
  
#end
