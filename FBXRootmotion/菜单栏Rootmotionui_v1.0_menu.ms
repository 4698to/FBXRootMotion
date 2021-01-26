(
	if ((menuMan.findMenu "FBX Rootmotion") != undefined) then
	(
		menuMan.unRegisterMenu (menuMan.findMenu "FBX Rootmotion")
		menuMan.updateMenuBar()
	)


	macroScript FBXRootmotion_max category:"FBX Rootmotion" buttonText: "FBX Rootmotion"
	(
		python.ExecuteFile((getDir #scripts) + "\\FBXRootmotion\\FBXRootmotionui_v1.0.py")
	)



	Main = menuMan.getMainMenuBar()
	Menu = menuMan.createMenu "FBX Rootmotion"
	theSubMenu = menuMan.createSubMenuItem "FBX Rootmotion" Menu
	Main.addItem theSubMenu (Main.numItems()+1)

	Action = menuMan.createActionItem "FBXRootmotion_max" "FBX Rootmotion"
	Menu.addItem Action (Menu.numItems() + 1 )

	menuMan.updateMenuBar()
)
