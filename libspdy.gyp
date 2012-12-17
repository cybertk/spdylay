# Copyright (c) 2012 cybertk.com. All rights reserved.

# TODO(kyan): Only android is support now.

{
  'targets': [
    {
      'target_name': 'libspdy',
      'type': '<(library)',

      'dependencies': [
        '<(DEPTH)/third_party/zlib/zlib.gyp:zlib',
      ],

      'defines': [
        # 'HAVE_CONFIG_H',
        'HAVE_ARPA_INET_H=0',
        'HAVE_DLFCN_H=0',
        'HAVE_INTTYPES_H=0',
        'HAVE_LIBXML2=0',
      ],

      'sources': [
        'lib/spdylay_buffer.c',
        'lib/spdylay_client_cert_vector.c',
        'lib/spdylay_frame.c',
        'lib/spdylay_gzip.c',
        'lib/spdylay_helper.c',
        'lib/spdylay_map.c',
        'lib/spdylay_npn.c',
        'lib/spdylay_outbound_item.c',
        'lib/spdylay_pq.c',
        'lib/spdylay_queue.c',
        'lib/spdylay_session.c',
        'lib/spdylay_stream.c',
        'lib/spdylay_submit.c',
        'lib/spdylay_zlib.c',
      ],

      'include_dirs': [
        'lib',
        'lib/includes',
        '.',
      ],
    },
  ],
}
