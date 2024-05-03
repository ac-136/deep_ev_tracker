given_string = "some_text_with_tracks_and_following_text"
substring_to_remove = "tracks"

# Find the position of the substring "tracks"
position = given_string.find(substring_to_remove)

# If the substring "tracks" is found, keep the portion of the string before it
# and include "tracks" itself in the modified string
if position != -1:
    modified_string = given_string[:position]
else:
    # If the substring "tracks" is not found, keep the original string
    modified_string = given_string

print(modified_string)