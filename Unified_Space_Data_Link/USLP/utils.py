from . import *


def buildTransferFrame(transfer_frame_version_number,
                       spacecraft_ID,
                       source_or_destination_ID,
                       virtual_channel_ID,
                       multiplexer_access_point_ID,
                       end_of_frame_primary_header_flag,
                       data,
                       TFDZ_construction_rules=None,
                       USLP_protocol_identifier=None,
                       first_header_last_valid_octet_pointer=None,
                       frame_length=None,
                       bypass_sequence_control_flag=None,
                       command_control_flag=None,
                       spare=None,
                       operational_control_field_flag=None,
                       virtual_channel_sequence_counter_length=None,
                       virtual_channel_sequence_counter_value=None,
                       insert_zone=None,
                       operational_control_field=None,
                       error_control_field=None
                       ):

    if end_of_frame_primary_header_flag == 0:
        header = TransferFramePrimaryHeader.TransferPrimaryHeader(transfer_frame_version_number,
                                                                  spacecraft_ID,
                                                                  source_or_destination_ID,
                                                                  virtual_channel_ID,
                                                                  multiplexer_access_point_ID,
                                                                  end_of_frame_primary_header_flag,
                                                                  frame_length,
                                                                  bypass_sequence_control_flag,
                                                                  command_control_flag,
                                                                  spare,
                                                                  operational_control_field_flag,
                                                                  virtual_channel_sequence_counter_length,
                                                                  virtual_channel_sequence_counter_value)

        dataFieldHeader = TransferFrameDataFieldHeader.TransferFrameDataFieldHeader(TFDZ_construction_rules,
                                                                                    USLP_protocol_identifier,
                                                                                    first_header_last_valid_octet_pointer)

        dataField = TransferFrameDataField.TransferFrameDataField(dataFieldHeader, data)

        return TransferFrame.TransferFrame(header, insert_zone, dataField, operational_control_field,
                                           error_control_field)

    else:
        header = TruncatedTransferFramePrimaryHeader.TruncatedTransferFramePrimaryHeader(transfer_frame_version_number,
                                                                                         spacecraft_ID,
                                                                                         source_or_destination_ID,
                                                                                         virtual_channel_ID,
                                                                                         multiplexer_access_point_ID,
                                                                                         end_of_frame_primary_header_flag)

        dataFieldHeader = TransferFrameDataFieldHeader.TransferFrameDataFieldHeader(TFDZ_construction_rules,
                                                                                    USLP_protocol_identifier,
                                                                                    first_header_last_valid_octet_pointer)

        dataField = TransferFrameDataField.TransferFrameDataField(dataFieldHeader, data)

        return TruncatedTransferFrame.TruncatedTransferFrame(header, dataField)
