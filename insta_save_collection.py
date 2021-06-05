import instaloader


def insta_save():
	username ="_webdevelopers"
	loader = instaloader.Instaloader()
	loader.load_session_from_file(username)
	profile = instaloader.Profile.from_username(loader.context,username)

	arr = []
	for saved_data in profile.get_saved_posts():
		arr.append(saved_data)

	loader.download_post(arr[0],'my_saved_collections')

	insta_save()


insta_save()