python.Init()
(
	if ((menuMan.findMenu "FBX Rootmotion") != undefined) then
	(
		menuMan.unRegisterMenu (menuMan.findMenu "FBX Rootmotion")
		menuMan.updateMenuBar()
	)

)
