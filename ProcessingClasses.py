'''------------------------------------------
Title: Processing Classes
Desc: A Module for processing Classes
DBiesinger, 2020-Jan-01, Created File
DBiesinger, 2020-Jan-02, Extended functionality to add tracks
Jeffrey Shen, 2020-Mar-20, added to select and add function
Jeffrey Shen, 2022-Mar-20, debugged/edited code
------------------------------------------'''

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        try:
            # set int cd_idx
            cd_idx = int(cd_idx)
            for row in table:
                # find each cd_id in table
                if row.cd_id == cd_idx:
                    return row
                # set exception if not in list
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd

        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the track gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        # set variables into tuple
        trkPos, trkTitle, trkLength = track_info
        try:
            # check if position is an integer
            if type(trkPos) == int:
                # set track to data class module, track class
                track = DC.Track(trkPos, trkTitle, trkLength)
                # add tracks to cd instance
                cd.add_track(track)
        except Exception as e:
            raise Exception(str(e))