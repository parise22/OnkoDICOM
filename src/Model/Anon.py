#### THE Anonymization function for the patient identifiers #########

import csv
import logging
import os
import uuid

import pandas as pd
import pydicom

from src.Model.CalculateDVHs import dvh2csv

# ========================================Anonymization code ===================================


## ===================================HASH Function================================================


def _hash_identifiers(file_no, ds_rtss):
    """in place anonymisation of a set of identifiers in a dataset
    Parameters
    ----------
    file_no: ``int``
        control parameter to dictate whether some of the returned parameters
        are set to 0.  If this is set to 1, the return parameters are not set to 0.
        In practice, this is used so that the first dataset in a collection 
            is treated differently
    
    ds_rtss: ``pydicom.dataset.Dataset``
        A dataset to be anonymised

    Returns
    -------
    p_name_plus_id: ``str``
        Concatenation of incoming PatientName, the string " + ", and the PatientID
        If file_no passed in was not 1, the string "0"
    hashed_patient_name: ``str``
        The anonymised patient name (only the patient name, not the p_name_plus_id)

    file_no_equals_one: ``int``
        1 if file_no passed in was 1, 0 otherwise
      
    """

    # ------------------------------------Sha1 hash for patient name-------------------------------------

    if "PatientName" in ds_rtss:
        patient_name = str(ds_rtss.PatientName)
        # print("Patient name - ", patient_name)
        # MD 5 hashing
        hash_patient_name_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, patient_name)
        # Hashing the MD5 hash again using SHA1
        hash_patient_name_sha1 = uuid.uuid3(
            uuid.NAMESPACE_URL, str(hash_patient_name_MD5)
        )
        # storing the hash to dataset
        ds_rtss.PatientName = str(hash_patient_name_sha1)
    else:
        logging.warning("No patient name found in RT SS: %s", ds_rtss["SOPInstanceUID"])
        print("NO patient Name found")

    # -----------------------------------------sha1 hash for patient ID------------------------------

    # if 'PatientID' in ds_rtss:
    if "PatientID" in ds_rtss:
        patient_ID = str(ds_rtss.PatientID)
        # print("Patient ID - ", patient_ID)
        # MD 5 hashing
        hash_patient_ID_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, patient_ID)
        # Hashing the MD5 hash again using SHA1
        hash_patient_ID_sha1 = uuid.uuid3(uuid.NAMESPACE_URL, str(hash_patient_ID_MD5))
        # storing the hash to dataset
        ds_rtss.PatientID = str(hash_patient_ID_sha1)
    else:
        print("NO patient ID not found")

    # #  storing patient_name and ID in one variable
    # if hasattribute("PatientID", ds_rtss):
    #     P_name_ID = patient_name + " + " + patient_ID
    # else:
    #     P_name_ID = patient_name + " + " + "PID_empty"

    # ----------------------------------------------sha1 hash for patient DOB---------------------------------------

    if "PatientBirthDate" in ds_rtss:
        patient_DOB = str(ds_rtss.PatientBirthDate)
        # print("Patient DOB - ", patient_DOB)
        # MD 5 hashing
        hash_patient_DOB_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, patient_DOB)
        # Hashing the MD5 hash again using SHA1
        hash_patient_DOB_sha1 = uuid.uuid3(
            uuid.NAMESPACE_URL, str(hash_patient_DOB_MD5)
        )
        # storing the hash to dataset
        ds_rtss.PatientBirthDate = str(hash_patient_DOB_sha1)
    else:
        print("Patient BirthDate not found")

    # --------------------------------------------sha1 hash for patient Sex------------------------------------

    if "PatientSex" in ds_rtss:
        patient_sex = str(ds_rtss.PatientSex)
        # print("Patient Sex - ", patient_sex)
        # MD 5 hashing
        hash_patient_Sex_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, patient_sex)
        # Hashing the MD5 hash again using SHA1
        hash_patient_Sex_sha1 = uuid.uuid3(
            uuid.NAMESPACE_URL, str(hash_patient_Sex_MD5)
        )
        # storing the hash to dataset
        ds_rtss.PatientSex = str(hash_patient_Sex_sha1)
    else:
        print("Patient Sex not found")

    # ----------instance creation------------

    if "InstanceCreationDate" in ds_rtss:
        Instance_creation_Date = str(ds_rtss.InstanceCreationDate)
        # print("Patient Sex - ", patient_sex)
        # MD 5 hashing
        hash_Instance_creation_Date_MD5 = uuid.uuid5(
            uuid.NAMESPACE_URL, Instance_creation_Date
        )
        # Hashing the MD5 hash again using SHA1
        hash_Instance_creation_Date_sha1 = uuid.uuid3(
            uuid.NAMESPACE_URL, str(hash_Instance_creation_Date_MD5)
        )
        # storing the hash to dataset
        ds_rtss.InstanceCreationDate = str(hash_Instance_creation_Date_sha1)
    else:
        print("Instance Creation date not found")

    # -----------STUDY date--------------
    if "StudyDate" in ds_rtss:
        Study_Date = str(ds_rtss.StudyDate)
        # print("Patient Sex - ", patient_sex)
        # MD 5 hashing
        hash_Study_Date_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, Study_Date)
        # Hashing the MD5 hash again using SHA1
        hash_Study_Date_sha1 = uuid.uuid3(uuid.NAMESPACE_URL, str(hash_Study_Date_MD5))
        # storing the hash to dataset
        ds_rtss.StudyDate = str(hash_Study_Date_sha1)
    else:
        print("Patient Study_Date not found")

    # -----------------content date date-----------
    if "ContentDate" in ds_rtss:
        Content_Date = str(ds_rtss.ContentDate)
        # print("Patient Sex - ", patient_sex)
        # MD 5 hashing
        hash_Content_Date_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, Content_Date)
        # Hashing the MD5 hash again using SHA1
        hash_Content_Date_sha1 = uuid.uuid3(
            uuid.NAMESPACE_URL, str(hash_Content_Date_MD5)
        )
        # storing the hash to dataset
        ds_rtss.ContentDate = str(hash_Content_Date_sha1)
    else:
        print("Patient Content_Date not found")

    # ------------------Structure set date-----------------

    if "StructureSetDate" in ds_rtss:
        Structure_Set_Date = str(ds_rtss.StructureSetDate)
        # print("Patient Sex - ", patient_sex)
        # MD 5 hashing
        hash_Structure_Set_Date_MD5 = uuid.uuid5(uuid.NAMESPACE_URL, Structure_Set_Date)
        # Hashing the MD5 hash again using SHA1
        hash_Structure_Set_Date_sha1 = uuid.uuid3(
            uuid.NAMESPACE_URL, str(hash_Structure_Set_Date_MD5)
        )
        # storing the hash to dataset
        ds_rtss.StructureSetDate = str(hash_Structure_Set_Date_sha1)
    else:
        print("Patient Content_Date not found")

    # used to return flag = 1 to indicate the first file is used for saving the hash in
    # hash_CSV file so CSV function will not be performed for rest of the files.
    if file_no == 1:
        if "PatientID" in ds_rtss:
            P_name_ID = patient_name + " + " + patient_ID
            print("Pname and ID=   ", P_name_ID)
        else:
            P_name_ID = patient_name + " + " + "PID_empty"
            print("Pname and ID=   ", P_name_ID)
        return (P_name_ID, hash_patient_name_sha1, 1)
    else:
        return (0, hash_patient_name_sha1, 0)


## ===================================CHECK FILE EXIST================================================


def _check_identity_mapping_file_exists(fileName):
    """
    Determine if the unqualified name specified has a corresponding file
    in a partially qualified path relative to the current working directory.

    Parameters
    ----------
    fileName: ``str``
    The unqualified name of the desired or already available CSV file.
    However, if the file name provided is not patientHash.csv, the file is
    treated as if it doesn't exist (no actual check takes place).
    If the file name is patientHash.csv, then the partially qualified
    path src/data/csv/patientHash.csv relative to the current working directory
    will be utilised.

    Returns
    -------
    file_is_present: ``bool``
    fully qualified path: ``str``
        optionally returned, only if parameter had value "patientHash.csv"
    """
    print("file name:-- ", fileName)  # printing file name

    if fileName == "patientHash.csv":
        data_folder_path = "/src/data/csv/"
        cwd = os.getcwd()  # getting the current working directory
        file_path = (
            cwd + data_folder_path + fileName
        )  # concatenating the current working directory with the csv filename
        print("Full path :  ===========", file_path)  # print the full csv file path
        print(
            "file exist: ", os.path.isfile(file_path)
        )  # check if the file exist in the folder
        if (os.path.isfile(file_path)) == True:  # if file exist return True
            print("returning true-----------------------")
            return True, file_path
        else:
            print(
                "returning false----------------------"
            )  # if file not exist return false
            return False, file_path


def _create_reidentification_spreadsheet(pname, sha1_pname, csv_filename):
    """ Creates or appends a csv file whose rows contain
    the original patient identifer and the anonymised identifier

    Parameters
    ----------
    pname: ``str``
            The original patient identifer

    sha1_pname: ``str``
            The anonymised identifier

    csv_filename: ``str``
            The unqualified name of the desired or already available CSV file.
            However, if the file name provided is not patientHash.csv, the file will be 
            overwritten.  If the file name is patientHash.csv, then the partially qualified
            path src/data/csv/patientHash.csv relative to the current working directory
            will be utilised.  If the partially qualified path does not already exists,
            an error is raised.

    Returns
    -------
      
    """
    # print("Csv file name is : ",csv_filename)
    # chcek if the patientHash.csv exist
    Csv_Exist, csv_filePath = _check_identity_mapping_file_exists(csv_filename)

    # if the csv doent exist create a new CSV and export the Hash to that.
    if Csv_Exist == False:
        print("-----Creating CSV------")

        csv_header = []
        csv_header.append("Pname and ID")
        csv_header.append("Hashed_Pname")
        print("the headers are:--", csv_header)

        # hash_dictionary =  {patient_ID : hash_patient_ID}
        # print("dictionary values",hash_dictionary)

        row = [pname, sha1_pname]
        sheet = []
        sheet.append(row)
        df_identifier_csv = pd.DataFrame(columns=csv_header).round(2)

        print("The CSV dataframe is:::", df_identifier_csv)
        print("---")
        print(csv_filePath)
        df_identifier_csv.to_csv(csv_filePath, index=False)  # creating the CVS

        with open(csv_filePath, "a") as csvFile:  # inserting the hash values
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()

        # print("The dataframe",df_identifier_csv)
        print("---------CSV created-----------")
        # options()

    else:
        print("updating csv")
        row = [pname, sha1_pname]
        with open(csv_filePath, "a") as csvFile:  # updating the CVS with hash values
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()
        print("------CSV updated -----")


# ====================== getting Modality and Instance_number for new dicom file name=========
def _get_modality_ins_num(ds):

    modality = ds.Modality
    if modality == "RTSTRUCT" or (modality == "RTPLAN"):
        return modality, 0
    else:
        Inum = str(ds.InstanceNumber)
        return modality, Inum


# ===================================Writing the hashed identifiers to DICOM FILE================================================
def _write_hash_dcm(
    ds_rtss, Dicom_folder_path, Dicom_filename, sha1_P_name, new_patient_folder_name
):

    modality, Inum = _get_modality_ins_num(ds_rtss)

    SecondLastDir = os.path.dirname(
        Dicom_folder_path
    )  # getting path till the second last Folder

    # writing the New hashed dicom file with new name "Modality_Instance-Number_Hashed.dcm"
    if modality == "RTSTRUCT":
        # # Adding Prefix "Hashed " for each anonymized Dicom file and concat the file and folder
        full_path_new_file = (
            SecondLastDir
            + "/"
            + new_patient_folder_name
            + "/"
            + modality
            + "_"
            + "Hashed"
            + ".dcm"
        )
        print("File name prefix with (Hashed) ", full_path_new_file)

        ds_rtss.save_as(full_path_new_file)
        print(":::::::Write complete :::")
    elif modality == "RTPLAN":
        # # Adding Prefix "Hashed " for each anonymized Dicom file and concat the file and folder
        full_path_new_file = (
            SecondLastDir
            + "/"
            + new_patient_folder_name
            + "/"
            + modality
            + "_"
            + "Hashed"
            + ".dcm"
        )
        print("File name prefix with (Hashed) ", full_path_new_file)

        ds_rtss.save_as(full_path_new_file)
        print(":::::::Write complete :::")
    else:
        # # Adding Prefix "Hashed " for each anonymized Dicom file and concat the file and folder
        full_path_new_file = (
            SecondLastDir
            + "/"
            + new_patient_folder_name
            + "/"
            + modality
            + "_"
            + str(Inum)
            + "_"
            + "Hashed"
            + ".dcm"
        )
        print("File name prefix with (Hashed) ", full_path_new_file)

        ds_rtss.save_as(full_path_new_file)
        print(":::::::Write complete :::")


# ## ===================================PRINTING THE HASH VALUES================================================


def _print_patient_identifiers(ds_rtss):
    print("INSIDE PRINT================")
    print("Patient name in dataset not hash: ", ds_rtss.PatientName)
    print("Patient ID in dataset not hash: ", ds_rtss.PatientID)
    print("Patient DOB in dataset not hash: ", ds_rtss.PatientBirthDate)
    print("Patient SEX in dataset not hash: ", ds_rtss.PatientSex)
    print("\n\n")


def _is_directory(file_path):
    return os.path.isdir(file_path)


# ==============Check in patient identifiers are already hashed===========


def _check_file_hashed(file_name, new_dict_dataset, key, matching_text):
    """Returns whether the file_name contains the matching text
    and the PatientName in the dataset pointed to by the key in the dict of datasets

    Parameters
    ----------
    file_name: ``str``
        the name of the DICOM file

    new_dict_dataset: ``dict`` with key of type ``str``|``int``, value of type pydicom.dataset.Dataset
        dict of the Patient's DICOM data objects

    key: ``str``|``int``
        key in to new_dict_dataset identifying which dataset to use for finding the 
        PatientsName which is presumed to be Hashed
    
    matching_text: ``str``
        the text that indicates whether the file contains hashed data or not based on
    the assumption that the filename will contain the text if it contains hashed data.

    Returns
    -------
    is_hashed, hashed_patient_name: ``bool``, ``str``|``int``
        True when matching_text in file_name, PatientName presumed to be hashed | 0
    """
    if matching_text in file_name:
        hash_value = new_dict_dataset[key].PatientName
        return True, hash_value
    else:
        return False, 0


def _create_anonymised_patient_folder(new_patient_folder_name, Dicom_folder_path):
    """Create the folder in which the anonymised patient's data will be placed

    Parameters
    ----------
    new_patient_folder_name : ``str``
        the unqualified path of the anonymised patient
    Dicom_folder_path : ``str``
        the fully or partially (relative to cwd) qualified path to the current patient's data
    """
    # getting the current working directory
    # Dicom_file_dir = os.getcwd()
    # Dicom_folder_path = self.path
    SecondLastDir = os.path.dirname(
        Dicom_folder_path
    )  # getting path till the second last Folder
    # concatinating the full path of the folder to store hashed files
    Full_Path_Patient_folder_new = SecondLastDir + "/" + new_patient_folder_name
    print("Full path patient new folder======", Full_Path_Patient_folder_new)

    # creating the new folder
    os.makedirs(
        Full_Path_Patient_folder_new
    )  # creating the new folder for New hashed files

    print("==================NEW FOLDER CREATED=========", Full_Path_Patient_folder_new)
    print("\n\n")
    # src_files = os.listdir(source_path)


# ========================CHECK if hashed FOLDER exist=======================================


def _anonymisation_folder_exists(
    new_dict_dataset, all_filepaths, Dicom_folder_path, File_hash_status
):

    """check if the directory of the hashed patient's name exists in the specified folder
    current implementation uses a hash of the PatientName for the name of the folder
    in which to place all of the patient's anonymised data, parallel to the directory
    containing the original not anonymised patient data.

    Parameters
    ----------
    new_dict_dataset: ``dict`` where values are ``pydicom.dataset.Dataset``
        dictionary of the DICOM data objects for the patient

    all_filepaths: ``list`` of str
        list of the paths to the files containing the DICOM objects in new_dict_dataset
    
    Dicom_folder_path:  ``str``
        the directory containing the current patient's DICOM data
    
    File_hash_status: ``int`` 
        representing a boolean indicating whether the datasets in new_dict_dataset
        have already been anonymised. 0 is False.

    Return
    ------
        directory_exists: ``int`` as boolean 

        anonymisation_folder_name:  ``str``
            unqualified path, hashed patient name

        fully_qualified_anonymisation_folder_name: ``str``

    """

    first_file = os.path.basename(all_filepaths[0])
    # print("THE PATH IN THE CHECK FOLDER::::::::::", all_filepaths[0] )
    if File_hash_status == 0:

        # ds_rtss = LOAD_DCM(Dicom_folder_path, first_file, new_dict_dataset, 0)
        ds_rtss = new_dict_dataset[0]
        if "PatientName" in ds_rtss:
            patient_name_first = str(ds_rtss.PatientName)
            # MD 5 hashing
            hash_patient_name_MD5_first = uuid.uuid5(
                uuid.NAMESPACE_URL, patient_name_first
            )
            # Hashing the MD5 hash again using SHA1
            hash_patient_name_sha1_first = uuid.uuid3(
                uuid.NAMESPACE_URL, str(hash_patient_name_MD5_first)
            )
            hash_patient_name_sha1_first = str(hash_patient_name_sha1_first)
        else:
            print("NO patient Name found")

        print(
            "Original patient name = =======================================",
            str(ds_rtss.PatientName),
        )
        print(
            "Original patient ID = =======================================",
            str(ds_rtss.PatientID),
        )
        print(
            "Original patient name = =======================================",
            str(ds_rtss.PatientBirthDate),
        )
        print(
            "Original patient name = =======================================",
            str(ds_rtss.PatientSex),
        )

        new_patient_folder_name = hash_patient_name_sha1_first
        print("New patient folder==", new_patient_folder_name)

        SecondLastDir = os.path.dirname(
            Dicom_folder_path
        )  # getting path till the second last Folder

        Full_Patient_Path_New_folder = SecondLastDir + "/" + new_patient_folder_name

        # check if the hashed Folder name exist in the Specified folder
        if new_patient_folder_name in os.listdir(SecondLastDir):
            return 1, new_patient_folder_name, Full_Patient_Path_New_folder
        else:
            return 0, new_patient_folder_name, Full_Patient_Path_New_folder
    else:
        SecondLastDir = os.path.dirname(
            Dicom_folder_path
        )  # getting path till the second last Folder

        # ds_rtss = LOAD_DCM(Dicom_folder_path, first_file, new_dict_dataset, 0)
        ds_rtss = new_dict_dataset[0]
        new_patient_folder_name = str(ds_rtss.PatientName)

        Full_Patient_Path_New_folder = SecondLastDir + "/" + new_patient_folder_name

        # check if the hashed Folder name exist in the Specified folder
        if new_patient_folder_name in os.listdir(SecondLastDir):
            return 1, new_patient_folder_name, Full_Patient_Path_New_folder
        else:
            return 0, new_patient_folder_name, Full_Patient_Path_New_folder


# ##==========================================Anon Function==========================================
def _anon_call(path, new_dict_dataset, all_filepaths):
    """create anonymised copies of DICOM data that are specified in a list of paths
    Parameters
    ----------
    path: ``str``
        The top level directory in which to create a subdirectory for the anonymised data

    new_dict_dataset: ``dict`` 
        keys are of type ``str`` and either DICOM Object type identifiers or integer value of count of 
        volumetric image slices.
        values are pydicom.dataset.Dataset

    all_filepaths: list of ``str``
        the items in the list are paths to the individual DICOM objects

    Returns
    -------
    anonymised_data_dirname: ``str``
        path to the anonymised data directory, (subdirectory of path parameter)
    """
    print("\n\n====Anon Called====")
    Dicom_folder_path = path

    # for key in new_dict_dataset:
    #     if key == 0:
    #         print("The values are : ", new_dict_dataset[key])

    # count = 0
    # for eachFile in All_dcm:
    #     count += 1

    First_Dicom_file = os.path.basename(all_filepaths[0])

    text = "Hashed"
    Is_hashed, hash_value = _check_file_hashed(
        First_Dicom_file, new_dict_dataset, 0, text
    )

    if Is_hashed != True:

        print("Is hashed: {} and the hash_value is: {}".format(Is_hashed, hash_value))
        (
            Exist_folder,
            new_patient_folder_name,
            Full_Patient_Path_New_folder,
        ) = _anonymisation_folder_exists(
            new_dict_dataset, all_filepaths, Dicom_folder_path, 0
        )

        if Exist_folder == 0:

            print("Status of folder==========", Exist_folder)
            print("The hashed folder does not exist")
            print("======Creating the new Hashed patient Folder=======")
            _create_anonymised_patient_folder(
                new_patient_folder_name, Dicom_folder_path
            )  # calling create_folder function
            # print("Is hashed: {} and the hash_value is: {}".format(Is_hashed, hash_value))

            count = 0
            for key, dicom_obj in new_dict_dataset.items():
                count += 1

                # store the name of each dcm file in a variable
                Dicom_filename = os.path.basename(all_filepaths[key])
                print("\n\nHASHING FILE ::::::=== ", Dicom_filename)

                # ds_rtss = new_dict_dataset[key]

                # print("\nMOdality is:   ", ds_rtss.Modality)
                # print("\nInstance Number is:   ", ds_rtss.InstanceNumber)

                # concatinating the folder path and the filename
                Full_dicom_filepath = Dicom_folder_path + "/" + Dicom_filename

                path_is_directory = _is_directory(Full_dicom_filepath)

                if not path_is_directory:

                    print(
                        "{} is an individual file, and not a directory".format(
                            Dicom_filename
                        )
                    )

                    # loading the dicom file content into the dataframe.
                    # ds_rtss = LOAD_DCM(
                    #    Dicom_folder_path, Dicom_filename, new_dict_dataset, key
                    # )
                    ds_rtss = dicom_obj
                    print("\n\nloaded in ds_rtss:============ ", Dicom_filename)

                    # calling the HASH function and it returns the (Pname + PID), (hashvalue) and
                    # (flag = 1  will be used to restrict only one hash value per patient in the CSV file)
                    pname_ID, sha1_pname, flag = _hash_identifiers(count, ds_rtss)
                    print(
                        "Patient name + ID=  {} and SHA1_name: {}".format(
                            pname_ID, sha1_pname
                        )
                    )

                    if (
                        flag == 1
                    ):  # (flag = 1 that will be used to restrict only one hash per patient in the CSV file)
                        print("\n\nFLAG --1111111111111111111111111")
                        print(
                            "Patient name + ID=  {} and SHA1_name: {}".format(
                                pname_ID, sha1_pname
                            )
                        )

                        _print_patient_identifiers(
                            ds_rtss
                        )  # calling the print to show the identifiers
                        csv_filename = "patientHash.csv"
                        # calling create CSV to store the the hashed value
                        _create_reidentification_spreadsheet(
                            pname_ID, sha1_pname, csv_filename
                        )
                        print("Updating patient re-identification spreadsheet")

                        _write_hash_dcm(
                            ds_rtss,
                            Dicom_folder_path,
                            Dicom_filename,
                            sha1_pname,
                            new_patient_folder_name,
                        )
                    else:
                        print("\n\nFLAG --0000000000000000000000000")
                        print("already updated patient re-identification spreadsheet")
                        print("Saving anonymised DICOM data")
                        # write_hash_dcm(sha1_pname, Dicom_filename)
                        _write_hash_dcm(
                            ds_rtss,
                            Dicom_folder_path,
                            Dicom_filename,
                            sha1_pname,
                            new_patient_folder_name,
                        )
                else:
                    print(
                        "\n\n\n======File {} is a Folder=====".format(Dicom_filename)
                    )  #     write_hash_dcm(ds_rtss, Dicom_folder_path , Dicom_filename, sha1_pname)
                    print("\n\n\n")
            print("Total files hashed======", count)
            return Full_Patient_Path_New_folder
        else:
            print(
                "This directory have already been hashed, it is directory ({}). Have overwritten that directory with the new files.".format(
                    new_patient_folder_name
                )
            )
            count = 1
            for key, dicom_object in new_dict_dataset.items():

                Dicom_filename = os.path.basename(all_filepaths[key])
                # ds_rtss = LOAD_DCM(
                #     Dicom_folder_path, Dicom_filename, new_dict_dataset, key
                # )
                ds_rtss = dicom_object
                pname_ID, sha1_pname, flag = _hash_identifiers(count, ds_rtss)
                _write_hash_dcm(
                    ds_rtss,
                    Dicom_folder_path,
                    Dicom_filename,
                    hash_value,
                    new_patient_folder_name,
                )
            count = 0
            print("Total files hashed======", count)
            print("\n\n============Overwrite complete==================")
            return Full_Patient_Path_New_folder
    else:

        print(
            "The files are already Hashed, need to export to the existing New patient folder"
        )

        (
            Exist_folder,
            new_patient_folder_name,
            Full_Patient_Path_New_folder,
        ) = _anonymisation_folder_exists(
            new_dict_dataset, all_filepaths, Dicom_folder_path, 1
        )

        for key, dicom_obj in new_dict_dataset.items():

            print(
                "Is hashed: {} and the hash_value is: {}".format(Is_hashed, hash_value)
            )
            print("Patient Identifiers already hashed")
            print("Just overwriting the files without hashing")

            # Exist_folder, new_patient_folder_name = check_folder_exist(new_dict_dataset, all_filepaths, Dicom_folder_path, 1)

            if Exist_folder == 0:
                print("Status of folder==========", Exist_folder)
                print("The hashed folder does not exist")
                print("======Creating the new Hashed patient Folder=======")
                _create_anonymised_patient_folder(
                    new_patient_folder_name, Dicom_folder_path
                )  # calling create_folder function
                Dicom_filename = os.path.basename(all_filepaths[key])
                # loading the dicom file content into the dataframe.
                # ds_rtss = LOAD_DCM(
                #    Dicom_folder_path, Dicom_filename, new_dict_dataset, key
                # )
                ds_rtss = dicom_obj
                _write_hash_dcm(
                    ds_rtss,
                    Dicom_folder_path,
                    Dicom_filename,
                    hash_value,
                    new_patient_folder_name,
                )
                count = 0
                print("Total files hashed======", count)
            else:
                print("Status of folder==========", Exist_folder)
                print("The hashed folder exist")
                Dicom_filename = os.path.basename(all_filepaths[key])
                # ds_rtss = LOAD_DCM(
                #    Dicom_folder_path, Dicom_filename, new_dict_dataset, key
                # )
                ds_rtss = dicom_obj
                _write_hash_dcm(
                    ds_rtss,
                    Dicom_folder_path,
                    Dicom_filename,
                    hash_value,
                    new_patient_folder_name,
                )
                count = 0
                print("Total files hashed======", count)
        return Full_Patient_Path_New_folder


def _has_child_CSV_directory(Full_Patient_Path_New_folder):
    if "CSV" in os.listdir(Full_Patient_Path_New_folder):
        return 1
    else:
        return 0


def anonymize(path, Datasets, FilePaths, rawdvh):
    """
    Create an anonymised copy of an entire patient data set, including
    DICOM files,
    DHV CSV file,
    Clinical Data CSV file,
    and place it in a subdirectory of the specified path

    Parameters
    ----------
    path: ``str``
        Directory in which to place a subdirectory containing the anonymised data

    Datasets: ``dict`` with values of ``pydicom.dataset.Dataset``
        The set of DICOM data for the patient to be anonymised

    Filepaths: ``list`` of ``string``
        The list of fully or partially qualified (relative to current working directory) filenames
        pointing to the patient's DICOM data

    rawdvh: ``dict`` with key = ROINumber, value = DVH 
        a representation of the Dose Volume Histogram 

    Returns
    -------
    Full_Patient_Path_New_folder: ``str``
        The fully qualified directory name where the anonymised data has been placed
    """

    all_filepaths = FilePaths
    new_dict_dataset = Datasets
    print("\n\nCurrent Work Directory is:  ==== ", os.getcwd())
    print("IN ANON===================")
    print("\n\n\n=====Path in ANONYMIZation   ===", path)
    # print("=====Datasets========= in ANONYMIZation   ===",Datasets)
    print("\n\n\n=====FilePaths in ANONYMIZation   ===", all_filepaths)
    # print("The value for CT 0 is : ", new_dict_dataset[0])
    # for key in Datasets:
    #     if (key != 'rtplan' and key != 'rtss' and key != 'rtdose'):
    #         print("Values are:  ",Datasets[key])

    Original_P_ID = new_dict_dataset[1].PatientID

    Full_Patient_Path_New_folder = _anon_call(path, new_dict_dataset, all_filepaths)
    print("\n\nThe New patient folder path is : ", Full_Patient_Path_New_folder)

    patient_hash_dvh = os.path.basename(Full_Patient_Path_New_folder)
    print("The HashID for DVh.hash is ::::", patient_hash_dvh)

    Full_Csv_Folder_Path = Full_Patient_Path_New_folder + "/" + "CSV"
    # check if CSV folder exist
    CSV_Folder_exist = _has_child_CSV_directory(Full_Patient_Path_New_folder)
    # if CSV folder does not exist create one
    if CSV_Folder_exist == 0:
        print("The CSV folder path is : ", Full_Csv_Folder_Path)
        os.makedirs(Full_Csv_Folder_Path)
        print("---CSV folder created---")
    else:
        print(":::The CSV folder exist:::")

    # SecondLastDir = os.path.dirname(path)  # getting path till the second last Folder
    # Full_Patient_Path_New_folder = SecondLastDir + "/" + "64246859-067c-3079-9703-7e71b6869232" + "/" + "CSV" + "/"

    Full_dvhCsv_Folder_Path_ = Full_Patient_Path_New_folder + "/" + "CSV" + "/"
    print("The path for dvh is::::::::::::::::  ", Full_dvhCsv_Folder_Path_)

    Dicom_filename = os.path.basename(all_filepaths[1])
    # ds_rtss = LOAD_DCM(path, Dicom_filename, new_dict_dataset, 1)
    ds_rtss = new_dict_dataset[1]
    # P_ID = ds_rtss.PatientID

    P_HashID = patient_hash_dvh

    print("The patient ID is ::::", P_HashID)

    dvh_csv_hash_name = "DVH_" + patient_hash_dvh

    # Calling dvh2csv() function after Anonymization is complete.
    print("CAlling DVH_csv export function")
    dvh2csv(rawdvh, Full_dvhCsv_Folder_Path_, dvh_csv_hash_name, P_HashID)
    print("DVH_csv export function finished\n\n")

    print("=======Calling Clinical data Export ==========")

    Clinical_data_original_file_name = "ClinicalData_" + Original_P_ID + ".csv"
    print("Clinical data file name to check: ", Clinical_data_original_file_name)

    clinical_data_CSV_origianl_path = path + "/" + "CSV"

    Clinical_data_csv_Full_file_path_orig = (
        clinical_data_CSV_origianl_path + "/" + Clinical_data_original_file_name
    )
    print(
        "The full path of clinical Data file to check:",
        Clinical_data_csv_Full_file_path_orig,
    )

    Clinical_data_hash_file_name = "ClinicalData_" + P_HashID + ".csv"
    Clinical_data_hash_csv_Full_file_path = (
        Full_Csv_Folder_Path + "/" + Clinical_data_hash_file_name
    )

    if "CSV" in os.listdir(path):
        print("The CSV folder Exist")
        if Clinical_data_original_file_name in os.listdir(
            clinical_data_CSV_origianl_path
        ):
            print("Need to hash the Clinical data file")

            ClinicalData_DF = pd.read_csv(Clinical_data_csv_Full_file_path_orig)
            print("The ClinicalData Dataframe is :::\n\n", ClinicalData_DF)

            P_count = ClinicalData_DF["PatientID"].count()
            print("The count of PatientId is ::::", P_count)

            for i in range(0, P_count):
                # ClinicalData_DF[]
                print(ClinicalData_DF.iloc[i, 0])
                print("Changing the value in dataframe")
                ClinicalData_DF.iloc[i, 0] = P_HashID
            print("The ClinicalData Dataframe after change is :::\n\n", ClinicalData_DF)
            ClinicalData_DF.to_csv(
                Clinical_data_hash_csv_Full_file_path, index=False
            )  # creating the Hashed clinical data CSV
            print("====Clinical data hash CSV Exported=====")

        else:
            print("The Clinical data file not yet exported")
    else:
        print("The CSV directory not Exist, and clinical data file is not exported")

    print("Clinical data function finished")

    return Full_Patient_Path_New_folder
