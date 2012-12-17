{
  'targets': [
    {
      'target_name': 'spdy-jni',
      'type': 'shared_library',

      'dependencies': [
        '<(DEPTH)/spdylay/libspdy.gyp:libspdy',
      ],
 
      'sources': [
        # Add jni codes here.
        'jni/com_cybertk_android_spdylay.cpp',
      ],
    }
  ],
}
