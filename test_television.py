import pytest
from television import Television

@pytest.fixture

def television():
    return Television()

def test_init(television):

    assert television._Television__status == False #Television off by default.
    assert television._Television__volume == Television.MIN_VOLUME
    assert television._Television__channel == Television.MIN_CHANNEL

def test_power(television):

    television.power() # Television should now be on.
    assert television._Television__status == True

    television.power() # Turning OFF TV.
    assert television._Television__status == False

def test_mute(television):

    television.mute()
    assert television._Television__muted == True

    television.mute()
    assert television._Television__muted == False

def test_channel_up(television):

    # Channel up while TV is off.
    assert television._Television__status == False
    television.channel_up()
    assert television._Television__channel == 0

    # Channel up while TV is on.
    television.power() # TV now ON
    assert television._Television__status == True
    television.channel_up()
    assert television._Television__channel == 1

    #Channel up while TV is on and CHANNEL is at MAX_CHANNEL.
    television.channel_up()
    television.channel_up()
    assert television._Television__channel == 3

    # At the channel max, any input past MAX_CHANNEL should wrap back to 0.
    television.channel_up()
    assert television._Television__channel == 0

def test_channel_down(television):

    # Channel up while TV is off.
    assert television._Television__status == False
    television.channel_down()
    assert television._Television__channel == 0

    # Channel down while TV is on. Should wrap back around to MAX_CHANNEL
    television.power()
    television.channel_down()
    assert television._Television__channel == 3

def test_volume_up(television):

    #TV is off and volume increased.
    assert television._Television__status == False
    television.volume_up()
    assert television._Television__volume == 0

    #TV is on and volume increased.
    television.power()
    assert television._Television__status == True
    television.volume_up()
    assert television._Television__volume == 1

    #TV is on, muted, and volume increased.
    television.mute()
    assert television._Television__muted == True
    television.volume_up()
    assert television._Television__muted == False
    assert television._Television__volume == 2

    #TV is on and increased past max volume (NEEDS FIXING)
    #television.volume_up()
    #assert television._Television__volume == 0

def test_volume_down(television):

    #TV is powered off and volume is decreased.
    assert television._Television__status == False
    television.volume_down()
    assert television._Television__volume == 0

    #TV is on and volume decreased from MAX_VOLUME

    television.power()
    assert television._Television__status == True

    television.volume_up()
    television.volume_up()
    assert television._Television__volume == 2

    television.volume_down()
    assert television._Television__volume == 1

    #TV is on, it is muted, and volume is decreased.
    television.mute()
    assert television._Television__muted == True
    television.volume_down()
    assert television._Television__muted == False
    assert television._Television__volume == 0

    # TV is on and decreased past MIN_VOLUME (NEEDS FIXING)
    # television.volume_down()
    # assert television._Television__volume == 2





