def diff(d1:dict, d2:dict, name1="dict1", name2="dict2") :
    """
    Compare deeply 2 objects and returns a dictionnary of the differences between them.
    This function expects two dicts but will work with (nested) lists, tuples, strings etc.

    The parameters `name1`and `name2` can be edited for lisibility of the output.

    WARNING : only native types are managed, and there is probably some cases that are not covered.
    
    The output is a dictionary that will countain the keys or indices that are different between the 2 objects.
    """
    diff_dict = {}
    if d1 == d2 :
        return diff_dict
    else :
        # for dict comparison, we check the diff for each common key
        # then we add to the diff dict all branches from one dict that are not in the other
        if isinstance(d1, dict) and isinstance(d2, dict) :
            
            common_keys = set(d1).intersection(set(d2))
            for key in common_keys :
                    d = diff(d1[key], d2[key], name1=name1, name2=name2)
                    if len(d) > 0 :
                        diff_dict[key] = d
            
            
            keys_only_d1 = set(d1).difference(set(d2))
            keys_only_d2 = set(d2).difference(set(d1))
            for keys, d, name in zip([keys_only_d1, keys_only_d2], [d1, d2], [name1, name2]) :
                if len(keys) != 0 :
                    diff_dict[name] = {}
                    for key in keys :
                        diff_dict[name].update({key : d[key]})

        # for comparison of lists and tuples, we check all elements by index
        # if they are of different sizes, we add a field to the diff dict with the additional elements    
        elif (
            (isinstance(d1, list) and isinstance(d2, list))
            or  (isinstance(d1, tuple) and isinstance(d2, tuple))
            ) :
            # comparison at equal index
            for i in range(max(len(d1), len(d2))) :
                try :
                    elmt1, elmt2 = d1[i], d2[i]
                except IndexError :
                    break
                else :
                    if elmt1 != elmt2:
                        diff_dict[f"index_{i}"] = diff(elmt1, elmt2, name1=name1, name2=name2)

            # if one sequence is longer than the other, we add the supplementary elements 
            for d, name, other_d in zip([d1, d2], [name1, name2], [d2, d1]) :
                if i >= len(d) :
                    diff_dict["supp_elmts"] = {name : list(other_d)[i:]}

            return diff_dict

        # for comparison of sets, strings, ints, floats...  
        else :
            if type(d1) == type(d2) :
                if d1 != d2 :
                    # if the elements to compare are non sequential or a string
                    if type(d1) in [str, float, int, complex] :
                        return {name1 : d1, name2 : d2}
                    # if the elements are sets
                    else :
                        elmts_1 = set(d1) - set(d2)
                        elmts_2 = set(d2) - set(d1)

                        for n, elmt in zip([name1, name2],  [elmts_1, elmts_2]) :
                            if len(elmt) > 0 :
                                diff_dict.update({n : elmt})
            else :
                diff_dict = {name1 : d1, name2 : d2}

        return diff_dict
