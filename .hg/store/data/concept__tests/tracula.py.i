        �        V���������g\�C�VK����EC����H            x��VMo�6�� ���`'͡A] ko6�n� v҃�D)\S�@Qn�_���p�]�P��7��ͣS%sEi�kŢ��J���x�e18�F�i_��&��3�y�7Ʋ�ɪ}��m�,d��"k�+��X)�5SZJQ5��^:��$T�&Er�`I���K|��(��~�
:��т�L���Ԛ�9��X)�p੒�EX S���kA�1��Vkw䰎����˧���f����/��7,�?~���_����ݧ����N'�@��~4ƋZ�;��M	�4J8F�*,�~
�I^�6W�1� ĝ��^�[�*e*Z�f�򎱰�K0��N�U�r� ��3��$����4�m6*̳�C�B4��:���^JS�{�y!��PH������)/0o�mE֎� ��y�A��'�ZN� ���'������<،�J��	%�IC^���BK�BP�f������5D��K�/��$L��:,͡B�~ט�ژ�29����E��$(ʰHL��~�piuSA�
�ZɅ�7�5	�s4�OW?����>TkV�R�f���8�����<�:7{��>�}tޫ�?��	.��'x�����@D[��c���1���]?VL����?H�o�~���E[R�W�o��I-t.�U�BW��5x.˽=�ɓ[��IS�iž��͹<QG*��>>=��i8�z�H~&Ӏt��ˉ�����O�y�c���º��vT[�g�oj]���)wP�`�Q�ډE�n�{�p�X�[��x�vI
����b���bČĠ�n:"S"j��1
���2a��N4g3o���X
�f+U�R	�+<-k/�F�Qw�22�kQ!^l;*jV�0��e{ !'�r��;_�W�����W��5��4V��=�탁Ye��	�#� ��5��[�>6:���98X�����t��@gM�� s�;���طb�;8���Yȋ�o���"\�Z�f[5��b�6�h`����f��T��l���>��椽�_c:�w����a?��s@!M@&��T�����M'���3ʀ�Rg��fMa�D��9Jm�He����i��oJ�ϟ?���!`}t������?�غ}���J�\h�W��IӮ;��U"���α0�K�����:���3�n6+Pz΄��X��y��j��<��^������    �    �        �    �������ߗ9�ئ 8�l�EK�9�            x���Ao�0����7�I(�rJTeE= �+�:����4Mo��YK��v
�q�čo�����O�{5ec��/Yy����f�}a^���MhٮCٴڸP�������Z�G�,����ד0�ሊ��y������Fkw���]QS�9��Z	*�y|��Md#��ZA-ݚ?��T	����� ߻�LU۹	8�8�\6�ѿ�I[�4��n�Tn[<�sh�cZ��`栖b��>����t���&wi0�m�`��O�vz�sb
����{�}��(6��=k����Lv������m�wPw��	��'/��o��n�(�:�V�43��؅�[('*�JYUQ���<J�Z	cE�0�؄��߽�C�k�����(M�J?���%��Q�Y�S�9#,���_ߍ�J�ƕ����3�*@A͌n��S��ֆ��x��I�C��~a׋
�\���Go��?���A�צ.����E��"��M��    �     0  �      �   ����wڝ�K�7�^��9.M��               �   �   $from vtk.util import numpy_support
    �     d  �      �   �����x�*c���"�h��/��M��              �     Xdata_dir = os.path.join(reader.get_data_root(),"freeSurfer_Tracula","%s"%SUBJ,"dpath")
    ;     Y  �      �   ����H� �tE���
w��4E�              
�     M    cont2 = reader.transform_points_to_space(cont,"diff",SUBJ,inverse=True)
    �     y  $          �����D�DV��Nn���P����B            x�c``x� �6iE��
IE�e�UzE��)�y)n�9%�Ez%E�y�i�E��
���E%
�9�!0a^.�" >
4�N�J��3sӍlєj@et�
�r2�s��2��4��2�R55y� �/�         Q  /      "   �������G�9��8�GܟϷv�j            x�c``x� �
iE��
IE�e�U
���E%
�%��%�EE��\�@�T+S��Z�Z�`�PT��V����� ��!    ^     J  1      u   �����cMJ~�ZNM�@U��O              �  
   >fa_img = reader.get("MRI",SUBJ,space="subject",format="vtk")
