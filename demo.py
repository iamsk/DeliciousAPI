import deliciousapi

dapi = deliciousapi.DeliciousAPI()

username = 'iamsk'

user_metadata = dapi.get_user(username, max_bookmarks=10)
print user_metadata
print user_metadata.bookmarks

user_tags = dapi.get_tags_of_user(username)
print user_tags

tag = 'python'
user_metadata_with_tag = dapi.get_user_with_tag(username,
                                                tag, max_bookmarks=10)
print user_metadata_with_tag
print user_metadata_with_tag.bookmarks
