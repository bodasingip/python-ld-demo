
import ldclient
from ldclient import Context
from ldclient.config import Config

# Set sdk_key to your LaunchDarkly SDK key before running
# sdk_key = "sdk-78ede243-f829-4c0a-8ed1-2c0e92892246"
sdk_key = "sdk-09738248-291d-4c1a-9aa2-4a9d077775ee"


# Set feature_flag_key to the feature flag key you want to evaluate
feature_flag_key = "contextAdd"

def show_message(s):
  print("*** %s" % s)
  print()

if __name__ == "__main__":
  if not sdk_key:
    show_message("Please edit main.py to set sdk_key to your LaunchDarkly SDK key first")
    exit()

  ldclient.set_config(Config(sdk_key))

  # The SDK starts up the first time ldclient.get() is called
  if ldclient.get().is_initialized():
    show_message("SDK successfully initialized!")
  else:
    show_message("SDK failed to initialize")
    exit()

  # Set up the evaluation context. This context should appear on your LaunchDarkly contexts
  # dashboard soon after you run the demo.
  context = Context.builder('test-user-key').name('Praveen').build()

  flag_value = ldclient.get().variation(feature_flag_key, context, False)

  show_message("Feature flag '%s' is %s for this context" % (feature_flag_key, flag_value))

  # Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
  # events to LaunchDarkly before the program exits. If analytics events are not delivered,
  # the context properties and flag usage statistics will not appear on your dashboard. In a
  # normal long-running application, the SDK would continue running and events would be
  # delivered automatically in the background.
  ldclient.get().close()