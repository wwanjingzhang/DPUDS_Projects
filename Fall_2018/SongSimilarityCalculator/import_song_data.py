"""
    import_song_data.py -- Prepares the million song dataset
    The entire dataset is 280 GB, so we'll use the 1.8 GB subset they provide
    The data subset contains 10,000 songs, each of which includes the following fields
        * artist_name
        * bars_start: shape = (99,) the number of bars a song has (99 in this example)
        * beats_start: shape = (397,) number of beats a song has
        * danceability: danceability measure of this song (according to the.echonest.org) 0 => not analyzed
        * duration (in seconds)
        * end_of_fade_in: time til end of fade-in at beginning of song (in seconds)
        * start_of_fade_out: start to of fade-out in seconds
        * energy: energy measure between 0 and 1 (0 => not analyzed)
        * key: estimation of the key the song is in
        * key_confidence: confidence of key estimation between 0 and 1
        * loudness: general loudness of song in dB
        * mode: estimation of the mode of the song (e.g. Lydian, Dorian, Aeolian, etc.)
        * release: album name from which the track was taken (always just one album)
        * sections_start: shape = (10,) start time of each section (verse, chorus, etc.) (this song has 10)
        * similar_artists: shape(100,) list of 100 similar artists according to the.echonest.org
        * song_hotttness: popularity of song from 0 to 1 based on when dataset is downloaded
        * tempo: tempo in BPM
        * time_signature: time signature in usual number of beats/bar
        * time_signature_confidence: confidence of signature value from 0 to 1
        * title
        * year
    There are many more fields, but we'll focus on these

    Dataset provided by:
        Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere.
        The Million Song Dataset. In Proceedings of the 12th International Society
        for Music Information Retrieval Conference (ISMIR 2011), 2011.
"""

import os
import sys
import time
import glob
import numpy as np
import hdf5_getters

# path to uncompressed song subset -- adjust to your local configuration
msd_path = 'D:\Programming\Python\MillionsongSubset'
msd_data_path = os.path.join(msd_path, 'data')
msd_addf_path = os.path.join(msd_path, 'AdditionalFiles')


# iterate over all files in all subdirectories
def apply_to_all_files(basedir, func=lambda x: x, ext='.h5'):
    '''
    :param basedir: base directory of the dataset
    :param func: function to apply to all filenames
    :param ext: extension, .h5 by default
    '''
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, '*'+ext))
        # count files
        for f in files:
            func(f)


# print out all song file locations
apply_to_all_files(msd_data_path, func=lambda x: print(x))

h5 = hdf5_getters.open_h5_file_read('D:\Programming\Python\MillionsongSubset\data\A\A\A\TRAAAAW128F429D538.h5')
artist = hdf5_getters.get_artist_name(h5)
title = hdf5_getters.get_title(h5)
print('Artist:', artist, '\nTitle:', title)
h5.close()
