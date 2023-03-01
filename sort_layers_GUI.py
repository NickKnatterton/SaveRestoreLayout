# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SortLayersDialogGUI
###########################################################################

class SortLayersDialogGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save/Restore Layout", pos = wx.DefaultPosition, size = wx.Size( 658,373 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.Size( 258,200 ), wx.DefaultSize )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Please match source and destination layers", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer14.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Source Layers", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText51.Wrap( -1 )

        bSizer181.Add( self.m_staticText51, 1, wx.ALL, 5 )

        self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Destination Layers", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText52.Wrap( -1 )

        bSizer181.Add( self.m_staticText52, 1, wx.ALL, 5 )

        self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Matched Layers", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText53.Wrap( -1 )

        bSizer181.Add( self.m_staticText53, 1, wx.ALL, 5 )


        bSizer14.Add( bSizer181, 0, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        list_src_layersChoices = []
        self.list_src_layers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), list_src_layersChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
        bSizer18.Add( self.list_src_layers, 1, wx.ALL|wx.EXPAND|wx.ALIGN_BOTTOM, 5 )

        list_dest_layersChoices = []
        self.list_dest_layers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_dest_layersChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
        bSizer18.Add( self.list_dest_layers, 1, wx.ALL|wx.EXPAND, 5 )

        list_matchesChoices = []
        self.list_matches = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_matchesChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
        bSizer18.Add( self.list_matches, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer14.Add( bSizer18, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Match", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer61.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button41 = wx.Button( self, wx.ID_ANY, u"Unmatch", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer61.Add( self.m_button41, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer61, 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn_cancel, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_ok = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn_ok, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer14.Add( bSizer6, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.list_src_layers.Bind( wx.EVT_LISTBOX, self.src_selected )
        self.list_src_layers.Bind( wx.EVT_LISTBOX_DCLICK, self.match_items )
        self.list_dest_layers.Bind( wx.EVT_LISTBOX, self.dest_selected )
        self.list_dest_layers.Bind( wx.EVT_LISTBOX_DCLICK, self.match_items )
        self.list_matches.Bind( wx.EVT_LISTBOX, self.match_selected )
        self.list_matches.Bind( wx.EVT_LISTBOX_DCLICK, self.unmatch_items )
        self.m_button4.Bind( wx.EVT_BUTTON, self.match_items )
        self.m_button41.Bind( wx.EVT_BUTTON, self.unmatch_items )
        self.btn_cancel.Bind( wx.EVT_BUTTON, self.cancel_restore )
        self.btn_ok.Bind( wx.EVT_BUTTON, self.continue_restore )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def src_selected( self, event ):
        event.Skip()

    def match_items( self, event ):
        event.Skip()

    def dest_selected( self, event ):
        event.Skip()


    def match_selected( self, event ):
        event.Skip()

    def unmatch_items( self, event ):
        event.Skip()



    def cancel_restore( self, event ):
        event.Skip()

    def continue_restore( self, event ):
        event.Skip()


